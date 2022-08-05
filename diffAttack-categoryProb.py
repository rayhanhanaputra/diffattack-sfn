
input_path = 'result.csv'

import multiprocessing as mp
import math
import json
import os

def calculate(inputs, outfile):
    probabilityTempMap = dict()

    for line in inputs:
        probability = int(float(line.split(',')[3].split('|')[0]))
        if(probabilityTempMap.__contains__(probability)):
            probabilityTempMap[probability] += 1
        else:
            probabilityTempMap[probability] = 1
    
    with open(outfile, 'w') as fp:
        json.dump(probabilityTempMap, fp)

if __name__ == "__main__":    

    input_file = open(input_path, "r")
    file_content = input_file.read()

    inputs = file_content.split("\n")[1:-1]
    inpLen = len(inputs)
    input_file.close()


    print('categorizing probability...')
    numOfProc = mp.cpu_count()-1
    procInpSize = inpLen / numOfProc
    
    processes = []
    processes.append(mp.Process(target=calculate,args=(inputs[:math.floor(procInpSize)],'tmp1.json')))
    
    a = 1
    for i in range(1,numOfProc-1):
        processes.append(mp.Process(target=calculate,args=(inputs[math.floor(i*procInpSize):math.floor((i+1)*procInpSize)],'tmp{}.json'.format(i+1))))
        a+=1
    processes.append(mp.Process(target=calculate,args=(inputs[math.floor(procInpSize*a):],'tmp{}.json'.format(a+1))))

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

    print('done')
    
    probabilityMap = dict()
    for i in range(numOfProc):
        tmpfilename = 'tmp{}.json'.format(i+1)
        with open(tmpfilename) as tmpfile:
            temp = json.load(tmpfile)
        os.remove(tmpfilename)
        for key in temp.keys():
            if(probabilityMap.__contains__(key)):
                probabilityMap[key] += temp[key]
            else:
                probabilityMap[key] = temp[key]
    
    for i in sorted(probabilityMap.keys()): 
        print("{}: {}".format(int(i),probabilityMap[i]))

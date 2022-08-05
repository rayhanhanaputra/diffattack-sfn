from itertools import product, combinations
import json
import time

ddtTable = [
    [16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 4, 0, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0],
    [0, 4, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 4, 2, 2, 2, 0, 0, 0, 2, 0, 2],
    [0, 2, 4, 2, 2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0],
    [0, 2, 0, 0, 2, 0, 0, 4, 0, 2, 4, 0, 2, 0, 0, 0],
    [0, 2, 0, 4, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 2],
    [0, 0, 0, 2, 0, 4, 0, 2, 0, 0, 0, 2, 0, 4, 2, 0],
    [0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
    [0, 0, 4, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 4, 0, 4],
    [0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 0, 4, 0, 2, 0, 2],
    [0, 0, 4, 0, 0, 2, 2, 0, 2, 2, 0, 0, 2, 0, 2, 0],
    [0, 0, 0, 2, 0, 0, 2, 4, 0, 0, 4, 2, 0, 0, 2, 0],
    [0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 4, 2],
    [0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 4, 2, 0, 0, 2, 4]
]


def S1Box(n):  # input n as a integer and it will return an sbox in hex value
    val = hex(n)

    if val == '0x0':
        return int(0xc)
    elif val == '0x1':
        return int(0xa)
    elif val == '0x2':
        return int(0xd)
    elif val == '0x3':
        return int(0x3)
    elif val == '0x4':
        return int(0xe)
    elif val == '0x5':
        return int(0xb)
    elif val == '0x6':
        return int(0xf)
    elif val == '0x7':
        return int(0x7)
    elif val == '0x8':
        return int(0x8)
    elif val == '0x9':
        return int(0x9)
    elif val == '0xa':
        return int(0x1)
    elif val == '0xb':
        return int(0x5)
    elif val == '0xc':
        return int(0x0)
    elif val == '0xd':
        return int(0x2)
    elif val == '0xe':
        return int(0x4)
    elif val == '0xf':
        return int(0x6)


def multiplyGF16(a, b):  # return the value of multiplication gf16 with 19 as the polynom
    arr = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [0, 2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 5, 11, 9, 15, 13],
        [0, 3, 6, 5, 12, 15, 10, 9, 11, 8, 13, 14, 7, 4, 1, 2],
        [0, 4, 8, 12, 3, 7, 11, 15, 6, 2, 14, 10, 5, 1, 13, 9],
        [0, 5, 10, 15, 7, 2, 13, 8, 14, 11, 4, 1, 9, 12, 3, 6],
        [0, 6, 12, 10, 11, 13, 7, 1, 5, 3, 9, 15, 14, 8, 2, 4],
        [0, 7, 14, 9, 15, 8, 1, 6, 13, 10, 3, 4, 2, 5, 12, 11],
        [0, 8, 3, 11, 6, 14, 5, 13, 12, 4, 15, 7, 10, 2, 9, 1],
        [0, 9, 1, 8, 2, 11, 3, 10, 4, 13, 5, 12, 6, 15, 7, 14],
        [0, 10, 7, 13, 14, 4, 9, 3, 15, 5, 8, 2, 1, 11, 6, 12],
        [0, 11, 5, 14, 10, 1, 15, 4, 7, 12, 2, 9, 13, 6, 8, 3],
        [0, 12, 11, 7, 5, 9, 14, 2, 10, 6, 1, 13, 15, 3, 4, 8],
        [0, 13, 9, 4, 1, 12, 8, 5, 2, 15, 11, 6, 3, 14, 10, 7],
        [0, 14, 15, 1, 13, 3, 2, 12, 9, 7, 6, 8, 4, 10, 11, 5],
        [0, 15, 13, 2, 9, 6, 4, 11, 1, 14, 12, 3, 8, 7, 5, 10]
    ]
    return arr[a][b]


def additionGF16(a, b):  # return the value of addition gf16
    arr = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],
        [2, 3, 0, 1, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13],
        [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12],
        [4, 5, 6, 7, 0, 1, 2, 3, 12, 13, 14, 15, 8, 9, 10, 11],
        [5, 4, 7, 6, 1, 0, 3, 2, 13, 12, 15, 14, 9, 8, 11, 10],
        [6, 7, 4, 5, 2, 3, 0, 1, 14, 15, 12, 13, 10, 11, 8, 9],
        [7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8],
        [8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7],
        [9, 8, 11, 10, 13, 12, 15, 14, 1, 0, 3, 2, 5, 4, 7, 6],
        [10, 11, 8, 9, 14, 15, 12, 13, 2, 3, 0, 1, 6, 7, 4, 5],
        [11, 10, 9, 8, 15, 14, 13, 12, 3, 2, 1, 0, 7, 6, 5, 4],
        [12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3],
        [13, 12, 15, 14, 9, 8, 11, 10, 5, 4, 7, 6, 1, 0, 3, 2],
        [14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 0, 1],
        [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ]
    return arr[a][b]


def mixColumns(mtrixST):  # mix columns in GF(16)
    M = [[1, 2, 6, 4], [2, 1, 4, 6], [6, 4, 1, 2], [4, 6, 2, 1]]
    newTrix = [[0 for x in range(4)] for y in range(4)]
    for i in range(0, 4):
        for j in range(0, 4):
            temp = multiplyGF16(M[i][0], mtrixST[0][j])
            temp2 = multiplyGF16(M[i][1], mtrixST[1][j])
            temp3 = multiplyGF16(M[i][2], mtrixST[2][j])
            temp4 = multiplyGF16(M[i][3], mtrixST[3][j])
            temp = additionGF16(temp, temp2)
            temp = additionGF16(temp, temp3)
            temp = additionGF16(temp, temp4)
            newTrix[i][j] = temp

    return newTrix


def mixRows(mtrixST):  # mix rows in GF(16)
    M = [[1, 2, 6, 4], [2, 1, 4, 6], [6, 4, 1, 2], [4, 6, 2, 1]]
    newTrix = [[0 for x in range(4)] for y in range(4)]
    for i in range(0, 4):
        for j in range(0, 4):
            temp = multiplyGF16(mtrixST[i][0], M[0][j])
            temp2 = multiplyGF16(mtrixST[i][1], M[1][j])
            temp3 = multiplyGF16(mtrixST[i][2], M[2][j])
            temp4 = multiplyGF16(mtrixST[i][3], M[3][j])
            temp = additionGF16(temp, temp2)
            temp = additionGF16(temp, temp3)
            temp = additionGF16(temp, temp4)
            newTrix[i][j] = temp

    return newTrix


def convertToMatrix(str):  # convert string of bits into 4x4 nibblesub
    matrixSTATE = [[0 for x in range(4)] for y in range(4)]
    iter = 0
    for i in range(0, 4):
        for j in range(0, 4):
            matrixSTATE[i][j] = int(str[iter:iter+4], 2)
            iter += 4

    return matrixSTATE


def convertToStr(mtrixST):  # convert 4x4 nibblesub into string of bits
    str = ""
    for i in range(0, 4):
        for j in range(0, 4):
            str = str + bin(mtrixST[i][j])[2:].zfill(4)
    return str


def split2(a):
    arr = [a >> 32]
    arr += [a & 0xffffffff]
    return arr


def split8(a):
    arr = []
    for i in range(8):
        arr += [(a >> 28-4*i) & 0xf]
    return arr


def split16(a):
    arr = split2(a)
    return split8(arr[0]) + split8(arr[1])


def split32(a):
    arr = []
    for i in range(32):
        arr += [(a >> 31-i) & 0b1]
    return arr


def join32(a):
    o = 0
    for i in range(len(a)):
        o = (o << 32) ^ a[i]
    return o


def join4(a):
    o = 0
    for i in range(len(a)):
        o = (o << 4) ^ a[i]
    return o


def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def calcActiveSBox(a):
    splat16 = split16(a)
    ind = 0
    act = []
    for s in splat16:
        if s != 0:
            act.append(ind)
        ind += 1

    return act


input = '2459528346497712128'
output_path = 'result.json'

# DIFF ATTACK ON SPN ENCRYPTION


def calculate(input, outfile):
    # GENERATE SBOX POSSIBLE OUTPUT DICT
    ddtDict = []
    for i in range(16):
        temp = {}
        for j in range(16):
            if(j > 0 and ddtTable[i][j] > 0 and bin(j).count('1') < 3):
                temp[j] = ddtTable[i][j]
        ddtDict.append(temp)

    f = open(outfile, 'w')

    input = int(input)

    output = {}
    output['input'] = input
    output['input(bin)'] = '{0:064b}'.format(input)

    # SBOX
    splat2 = split2(input)
    splat16 = split8(splat2[0]) + split8(splat2[1])
    subResult = []
    sboxActiveIndices = []
    counter = 0

    for i in splat16:
        subResult.append(list(ddtDict[i].keys()) if ddtDict[i] else 0)
        if i != 0:
            sboxActiveIndices.append(counter)
        counter += 1
    activeNibbles = list(filter(lambda nible: nible != 0, subResult))
    output['active nibbles sbox-round-1'] = activeNibbles

    if len(sboxActiveIndices) == 1:
        sboxOutputCombination = list(combinations(activeNibbles[0], 1))
    elif len(sboxActiveIndices) == 2:
        sboxOutputCombination = list(
            product(activeNibbles[0], activeNibbles[1]))
    elif len(sboxActiveIndices) == 3:
        sboxOutputCombination = list(
            product(activeNibbles[0], activeNibbles[1], activeNibbles[2]))
    elif len(sboxActiveIndices) == 4:
        sboxOutputCombination = list(
            product(activeNibbles[0], activeNibbles[1], activeNibbles[2], activeNibbles[3]))

    output['probabilities'] = []
    for curr in sboxOutputCombination:
        temp = {"choosen sbox output": str(curr)}
        sboxOutputProbability = [0 for i in range(16)]
        counter = 0
        probability = 1
        for i in sboxActiveIndices:
            sboxOutputProbability[i] = curr[counter]
            probability *= (ddtDict[splat16[i]][curr[counter]]/16)
            counter += 1

        a = join4(sboxOutputProbability)
        temp["after sbox"] = '{0:064b}'.format(a)

        mTrix = [[0 for x in range(4)] for y in range(4)]
        iter = 0
        for x in range(4):
            for y in range(4):
                mTrix[x][y] = sboxOutputProbability[iter]
                iter += 1

        a = mixColumns(mTrix)
        o = convertToStr(a)
        temp["after mixColumns"] = o

        a = mixRows(a)
        o = convertToStr(a)
        temp["after mixRows"] = o

        temp["probability"] = probability

        # SBOX round 2
        if(len(calcActiveSBox(int(o, 2))) < 5):
            splat2 = split2(int(o, 2))
            splat16 = split8(splat2[0]) + split8(splat2[1])
            subResult = []
            sboxActiveIndices = []
            counter = 0

            for i in splat16:
                subResult.append(list(ddtDict[i].keys()) if ddtDict[i] else 0)
                if i != 0:
                    sboxActiveIndices.append(counter)
                counter += 1
            activeNibbles = list(filter(lambda nible: nible != 0, subResult))
            output['active nibbles sbox-round-2'] = activeNibbles

            if len(sboxActiveIndices) == 1:
                sboxOutputCombination = list(combinations(activeNibbles[0], 1))
            elif len(sboxActiveIndices) == 2:
                sboxOutputCombination = list(
                    product(activeNibbles[0], activeNibbles[1]))
            elif len(sboxActiveIndices) == 3:
                sboxOutputCombination = list(
                    product(activeNibbles[0], activeNibbles[1], activeNibbles[2]))
            elif len(sboxActiveIndices) == 4:
                sboxOutputCombination = list(
                    product(activeNibbles[0], activeNibbles[1], activeNibbles[2], activeNibbles[3]))

            output['probabilities-round-2'] = []
            for curr in sboxOutputCombination:
                temp2 = {"choosen sbox-round-2 output": str(curr)}
                sboxOutputProbability = [0 for i in range(16)]
                counter = 0
                #probability = 1
                for i in sboxActiveIndices:
                    sboxOutputProbability[i] = curr[counter]
                    #probability *= (ddtDict[splat16[i]][curr[counter]]/16)
                    counter += 1

                a = join4(sboxOutputProbability)
                temp2["after sl.eox-round-2"] = '{0:064b}'.format(a)

                temp2["result"] = a

                temp2['active nibbles-sbox-round-2'] = calcActiveSBox(a)

                # temp["probability"] = probability

                output['probabilities-round-2'].append(temp2)
        ###

        output['probabilities'].append(temp)

    f.write(json.dumps(output))
    f.close()


start = time.time()
calculate(input, output_path)
end = time.time()
print("\nElapsed time :\t")
print(end - start)

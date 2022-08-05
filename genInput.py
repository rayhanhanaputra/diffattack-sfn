import itertools as it
import time

def join16(a):
    out = 0
    for i in range(len(a)):
        out = (out<<4) ^ a[i]
    return out

def check4FirstActiveNibble(s):
    s1 = s[:16]
    s2 = s[16:32]
    s3 = s[32:48]
    s4 = s[48:64]
    cek = False

    if s2.find("1") != -1:
        return False
    if s3.find("1") != -1:
        return False
    if s4.find("1") != -1:
        return False

    if s1.find("1") != -1:
        if s1[:4].find("1") != -1:
            if s1[4:8].find("1") != -1:
                if s1[8:12].find("1") != -1:
                    if s1[12:16].find("1") != -1:
                        return True
    return cek

def checkSameColumnActiveNibble(s):
    s1 = s[:4] + s[16:20] + s[32:36] + s[48:52]
    s2 = s[4:8] + s[20:24] + s[36:40] + s[52:56]
    s3 = s[8:12] + s[24:28] + s[40:44] + s[56:60]
    s4 = s[12:16] + s[28:32] + s[44:48] + s[60:64]

    if s1.find("1") != -1:
        temp = s2+s3+s4
        if temp.find("1") != -1:
            return False
    if s2.find("1") != -1:
        temp = s1+s3+s4
        if temp.find("1") != -1:
            return False
    if s3.find("1") != -1:
        temp = s1+s2+s4
        if temp.find("1") != -1:
            return False
    if s4.find("1") != -1:
        temp = s1+s2+s3
        if temp.find("1") != -1:
            return False

    return True    

output = []
sBoxes = range(16)

f = open('input.txt','w')

start = time.time()

# possibleNibbles = range(1,16)
# for comb in list(it.combinations(sBoxes, 1)):
#     for i in possibleNibbles:
#         out = [0 for j in range(16)]
#         out[comb[0]] = i
#         # f.write(bin(int(str(join16(out))))[2:].zfill(64)+'\n')
#         s = bin(join16(out))[2:].zfill(64)
#         if check4FirstActiveNibble(s):
#             f.write(str(join16(out))+'\n')
#         # f.write(str(join16(out))+'\n')


################################################
#
#INI GENERATE 2 ACTIVE NIBBLE DI KOLOM YANG SAMA
#
################################################
# possibleNibbles = list(it.product(range(1,16), range(1,16)))
# for comb in list(it.combinations(sBoxes, 2)):
#     for j in possibleNibbles:
#         out = [0 for j in range(16)]
#         idx = 0
#         for i in j:
#             out[comb[idx]] = i
#             idx += 1
#         # output.append(join16(out))
#         # f.write(str(join16(out))+'\n')
#         s = bin(join16(out))[2:].zfill(64)        
#         if checkSameColumnActiveNibble(s):
#             f.write(str(join16(out))+'\n')



################################################
#
#INI GENERATE 3 ACTIVE NIBBLE DI KOLOM YANG SAMA
#
################################################
# possibleNibbles = list(it.product(range(1,16), range(1,16), range(1,16)))
# for comb in list(it.combinations(sBoxes, 3)):
#     for j in possibleNibbles:
#         out = [0 for j in range(16)]
#         idx = 0
#         for i in j:
#             out[comb[idx]] = i
#             idx += 1
#         # output.append(join16(out))
#         # f.write(str(join16(out))+'\n')
#         s = bin(join16(out))[2:].zfill(64)        
#         if checkSameColumnActiveNibble(s):
#             f.write(str(join16(out))+'\n')

possibleNibbles = list(it.product(range(1,16), range(1,16), range(1,16), range(1,16)))
for comb in list(it.combinations(sBoxes, 4)):
    for j in possibleNibbles:
        out = [0 for j in range(16)]
        idx = 0
        for i in j:
            out[comb[idx]] = i
            idx += 1
        # f.write(bin(int(str(join16(out))))[2:].zfill(64)+'\n')
        # f.write(str(join16(out))+'\n')
        s = bin(join16(out))[2:].zfill(64)
        if check4FirstActiveNibble(s):
            f.write(str(join16(out))+'\n')

end = time.time()
print("\nElapsed time :\t")
print(end - start)
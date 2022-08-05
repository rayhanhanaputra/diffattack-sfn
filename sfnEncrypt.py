def S1Box(n): #input n as a integer and it will return an sbox in hex value
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

def S2Box(n): #input n as a integer and it will return an sbox in hex value
	val = hex(n)
	
	if val == '0x0':		
		return int(0xb)
	elif val == '0x1':
		return int(0xf)
	elif val == '0x2':
		return int(0x3)
	elif val == '0x3':
		return int(0x2)
	elif val == '0x4':
		return int(0xa)
	elif val == '0x5':
		return int(0xc)
	elif val == '0x6':
		return int(0x9)
	elif val == '0x7':
		return int(0x1)
	elif val == '0x8':
		return int(0x6)
	elif val == '0x9':
		return int(0x7)
	elif val == '0xa':
		return int(0x8)
	elif val == '0xb':
		return int(0x0)
	elif val == '0xc':
		return int(0xe)
	elif val == '0xd':
		return int(0x5)
	elif val == '0xe':
		return int(0xd)
	elif val == '0xf':
		return int(0x4)

def PBox(val): #parse the string 
	arr = [9,28,7,13,8,12,29,6,0,2,17,23,30,24,18,11,31,4,15,19,5,1,25,27,3,10,22,21,26,16,20,14]
	# var=["0" for i in range(len(val))]
	# for i in range(0,32):
	# 	var[arr[i]] = val[i] 
	# newstr = ""
	# for i in range(0,32):
	# 	newstr += var[i]
	newStr = ""
	for i in range(0,32):
		newStr+=val[arr[i]]
	return newStr

def multiplyGF16(a,b): #return the value of multiplication gf16 with 19 as the polynom
	arr = [
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10, 11 ,12 ,13 ,14 ,15],
		[0,2 ,4 ,6 ,8 ,10 ,12 ,14 ,3 ,1 ,7 ,5 ,11 ,9 ,15 ,13],
		[0,3 ,6 ,5 ,12 ,15 ,10 ,9 ,11 ,8 ,13 ,14 ,7 ,4 ,1 ,2],
		[0,4 ,8 ,12 ,3 ,7 ,11 ,15 ,6 ,2 ,14 ,10 ,5 ,1 ,13 ,9],
		[0,5 ,10 ,15 ,7 ,2 ,13 ,8 ,14 ,11 ,4 ,1 ,9 ,12 ,3 ,6],
		[0,6 ,12 ,10 ,11 ,13 ,7 ,1 ,5 ,3 ,9 ,15 ,14 ,8 ,2 ,4],
		[0,7 ,14 ,9 ,15 ,8 ,1 ,6 ,13 ,10 ,3 ,4 ,2 ,5 ,12 ,11],
		[0,8 ,3 ,11 ,6 ,14 ,5 ,13 ,12 ,4 ,15 ,7 ,10 ,2 ,9 ,1],
		[0,9 ,1 ,8 ,2 ,11 ,3 ,10 ,4 ,13 ,5 ,12 ,6 ,15 ,7 ,14],
		[0,10 ,7 ,13 ,14 ,4 ,9 ,3 ,15 ,5 ,8 ,2 ,1 ,11 ,6 ,12],
		[0,11 ,5 ,14 ,10 ,1 ,15 ,4 ,7 ,12 ,2 ,9 ,13 ,6 ,8 ,3],
		[0,12 ,11 ,7 ,5 ,9 ,14 ,2 ,10 ,6 ,1 ,13 ,15 ,3 ,4 ,8],
		[0,13 ,9 ,4 ,1 ,12 ,8 ,5 ,2 ,15 ,11 ,6 ,3 ,14 ,10 ,7],
		[0,14 ,15 ,1 ,13 ,3 ,2 ,12 ,9 ,7 ,6 ,8 ,4 ,10 ,11 ,5],
		[0,15 ,13 ,2 ,9 ,6 ,4 ,11 ,1 ,14 ,12 ,3 ,8 ,7 ,5 ,10]
	]
	return arr[a][b]

def additionGF16(a,b): #return the value of addition gf16
	arr = [
		[0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15],
		[1 ,0 ,3 ,2 ,5 ,4 ,7 ,6 ,9 ,8 ,11 ,10 ,13 ,12 ,15 ,14],
		[2 ,3 ,0 ,1 ,6 ,7 ,4 ,5 ,10 ,11 ,8 ,9 ,14 ,15 ,12 ,13],
		[3 ,2 ,1 ,0 ,7 ,6 ,5 ,4 ,11 ,10 ,9 ,8 ,15 ,14 ,13 ,12],
		[4 ,5 ,6 ,7 ,0 ,1 ,2 ,3 ,12 ,13 ,14 ,15 ,8 ,9 ,10 ,11],
		[5 ,4 ,7 ,6 ,1 ,0 ,3 ,2 ,13 ,12 ,15 ,14 ,9 ,8 ,11 ,10],
		[6 ,7 ,4 ,5 ,2 ,3 ,0 ,1 ,14 ,15 ,12 ,13 ,10 ,11 ,8 ,9],
		[7 ,6 ,5 ,4 ,3 ,2 ,1 ,0 ,15 ,14 ,13 ,12 ,11 ,10 ,9 ,8],
		[8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,0 ,1 ,2 ,3 ,4 ,5 ,6 ,7],
		[9 ,8 ,11 ,10 ,13 ,12 ,15 ,14 ,1 ,0 ,3 ,2 ,5 ,4 ,7 ,6],
		[10 ,11 ,8 ,9 ,14 ,15 ,12 ,13 ,2 ,3 ,0 ,1 ,6 ,7 ,4 ,5],
		[11 ,10 ,9 ,8 ,15 ,14 ,13 ,12 ,3 ,2 ,1 ,0 ,7 ,6 ,5 ,4],
		[12 ,13 ,14 ,15 ,8 ,9 ,10 ,11 ,4 ,5 ,6 ,7 ,0 ,1 ,2 ,3],
		[13 ,12 ,15 ,14 ,9 ,8 ,11 ,10 ,5 ,4 ,7 ,6 ,1 ,0 ,3 ,2],
		[14 ,15 ,12 ,13 ,10 ,11 ,8 ,9 ,6 ,7 ,4 ,5 ,2 ,3 ,0 ,1],
		[15 ,14 ,13 ,12 ,11 ,10 ,9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ,1 ,0]
	]
	return arr[a][b]

def addRoundKey(strST, roundKey):
	newStr = ""
	for i in range(len(strST)):
		newStr = newStr + xor(strST[i],roundKey[i],1)

	return newStr

def mixColumns(mtrixST): #mix columns in GF(16)
	M = [[1, 2, 6, 4], [2, 1, 4, 6], [6, 4, 1, 2], [4, 6, 2, 1]] 
	newTrix = [[0 for x in range(4)] for y in range(4)] 
	for i in range(0,4):
		for j in range(0,4):
			temp = multiplyGF16(M[i][0],int(mtrixST[0][j],2))
			temp2 = multiplyGF16(M[i][1],int(mtrixST[1][j],2))
			temp3 = multiplyGF16(M[i][2],int(mtrixST[2][j],2))
			temp4 = multiplyGF16(M[i][3],int(mtrixST[3][j],2))
			temp = additionGF16(temp,temp2)
			temp = additionGF16(temp,temp3)
			temp = additionGF16(temp,temp4)
			newTrix[i][j] = bin(temp)[2:].zfill(4)

	return newTrix
  
def mixRows(mtrixST): #mix rows in GF(16)
	M = [[1, 2, 6, 4], [2, 1, 4, 6], [6, 4, 1, 2], [4, 6, 2, 1]] 
	newTrix = [[0 for x in range(4)] for y in range(4)]
	for i in range(0,4):
		for j in range(0,4):
			temp = multiplyGF16(int(mtrixST[i][0],2),M[0][j])
			temp2 = multiplyGF16(int(mtrixST[i][1],2),M[1][j])
			temp3 = multiplyGF16(int(mtrixST[i][2],2),M[2][j])
			temp4 = multiplyGF16(int(mtrixST[i][3],2),M[3][j])
			temp = additionGF16(temp,temp2)
			temp = additionGF16(temp,temp3)
			temp = additionGF16(temp,temp4)
			newTrix[i][j] = bin(temp)[2:].zfill(4)

	return newTrix

def convertToMatrix(str): #convert string of bits into 4x4 nibblesub
	matrixSTATE = [[0 for x in range(4)] for y in range(4)] 
	iter = 0
	for i in range(0,4):
		for j in range(0,4):
			matrixSTATE[i][j] = str[iter:iter+4]
			iter+=4 

	return matrixSTATE

def convertToStr(mtrixST): #convert 4x4 nibblesub into string of bits
	str = ""
	for i in range(0,4):
		for j in range(0,4):
			str = str + mtrixST[i][j]
	
	return str

def xor(a, b, n): #xor ing a string of bits
    ans = ""
     
    # Loop to iterate over the
    # Binary Strings
    for i in range(n):
        
        # If the Character matches
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

def addConstants(key, iter): #adding CON based on the paper
	newKey = xor(key[:8],bin(iter)[2:].zfill(8),8) + key[8:]
	return newKey

def mixXors(s): #xor as defined
	new = ""
	new = new + xor(xor(xor(xor(xor(s[4:8],s[8:12],4),s[12:16],4),s[16:20],4),s[20:24],4),s[24:28],4)
	new = new + xor(xor(xor(xor(xor(s[0:4],s[8:12],4),s[12:16],4),s[20:24],4),s[24:28],4),s[28:32],4)
	new = new + xor(xor(xor(xor(xor(s[0:4],s[4:8],4),s[12:16],4),s[16:20],4),s[24:28],4),s[28:32],4)
	new = new + xor(xor(xor(xor(xor(s[0:4],s[4:8],4),s[8:12],4),s[16:20],4),s[20:24],4),s[28:32],4)
	new = new + xor(xor(xor(xor(s[0:4],s[4:8],4),s[12:16],4),s[16:20],4),s[20:24],4)
	new = new + xor(xor(xor(xor(s[0:4],s[4:8],4),s[8:12],4),s[20:24],4),s[24:28],4)
	new = new + xor(xor(xor(xor(s[4:8],s[8:12],4),s[12:16],4),s[24:28],4),s[28:32],4)
	new = new + xor(xor(xor(xor(s[0:4],s[8:12],4),s[12:16],4),s[16:20],4),s[28:32],4)

	return new

def encryptSPN(bits, rKey): #parse a string please
	newBits = bits[32:] + bits[:32]
	res = addRoundKey(newBits,rKey)
	matrixRes = convertToMatrix(res)
	for i in range(0,4):
		for j in range(0,4):
			if matrixRes[i][j] != '':
				matrixRes[i][j] = bin(S1Box(int(matrixRes[i][j],2)))[2:].zfill(4)
	matrixRes = mixColumns(matrixRes)
	matrixRes = mixRows(matrixRes)
	for i in range(0,4):
		for j in range(0,4):
			if matrixRes[i][j] != '':
				matrixRes[i][j] = bin(S1Box(int(matrixRes[i][j],2)))[2:].zfill(4)
	result = convertToStr(matrixRes)
	return result

def keyExpansionSPN(rKey, iter): #parse 64 bit of round key in a string and the iteration
	key = rKey[32:] + rKey[:32]
	key = addConstants(key, iter)
	rKeyInTrix = convertToMatrix(key) 
	for i in range(0,4):
		for j in range(0,4):
			if rKeyInTrix[i][j] != '':
				rKeyInTrix[i][j] = bin(S2Box(int(rKeyInTrix[i][j],2)))[2:].zfill(4)
	rKeyInTrix = mixColumns(rKeyInTrix)
	rKeyInTrix = mixRows(rKeyInTrix)
	for i in range(0,4):
		for j in range(0,4):
			if rKeyInTrix[i][j] != '':
				rKeyInTrix[i][j] = bin(S2Box(int(rKeyInTrix[i][j],2)))[2:].zfill(4)
	return convertToStr(rKeyInTrix)

def encryptFeistel(bits, rKey): #parse pre32bit rkey and 64 bit of text	
	preBit = bits[:32]
	postBit = bits[32:] 
	preInTrix = addRoundKey(preBit,rKey)
	preInTrix = convertToMatrix(preInTrix)
	for i in range(0,4):
		for j in range(0,4):
			if preInTrix[i][j] != '':
				preInTrix[i][j] = bin(S2Box(int(preInTrix[i][j],2)))[2:].zfill(4)
	preInTrix = PBox(convertToStr(preInTrix))
	preInTrix = mixXors(preInTrix)
	preInTrix = convertToMatrix(preInTrix)
	for i in range(0,4):
		for j in range(0,4):
			if preInTrix[i][j] != '':
				preInTrix[i][j] = bin(S2Box(int(preInTrix[i][j],2)))[2:].zfill(4)
	preBitNew = xor(convertToStr(preInTrix),postBit,32)
	return preBitNew+(bits[:32])

def keyExpansionFeistel(rKey, iter): #parse 64 bit key
	preBit = rKey[:32]
	postBit = rKey[32:] 
	preBit = addConstants(preBit, iter)
	preInTrix = convertToMatrix(preBit)
	for i in range(0,4):
		for j in range(0,4):
			if preInTrix[i][j] != '':
				preInTrix[i][j] = bin(S1Box(int(preInTrix[i][j],2)))[2:].zfill(4)
	preInTrix = PBox(convertToStr(preInTrix))
	preInTrix = mixXors(preInTrix)
	preInTrix = convertToMatrix(preInTrix)
	for i in range(0,4):
		for j in range(0,4):
			if preInTrix[i][j] != '':
				preInTrix[i][j] = bin(S1Box(int(preInTrix[i][j],2)))[2:].zfill(4)
	preBitNew = xor(convertToStr(preInTrix),postBit,len(postBit))
	return preBitNew+(rKey[:32])

#===================================================================
# MAIN PROGRAM
#===================================================================
def main(pt, ks):
	plaintext = pt
	keystream = ks
	ciphertext = plaintext

	roundKey = keystream[:64]
	signal = keystream[64:]

	print("Plainteks: "+plaintext)
	print("Keystream: "+keystream+"\n")

	for i in range(0,32):
		if signal[i] == '0':
			ciphertext = encryptSPN(ciphertext,roundKey)
			roundKey = keyExpansionFeistel(roundKey, i)
		elif signal[i] == '1':
			ciphertext = encryptFeistel(ciphertext,roundKey[:32])
			roundKey = keyExpansionSPN(roundKey, i)
		print("Round"+str(i)+"\t:"+ciphertext)
		print("Key\t:"+roundKey +"\n")

	ciphertext = ciphertext[32:] + ciphertext[:32]
	ciphertext = addRoundKey(ciphertext, roundKey)

	# print("Cipherteks:\t"+ciphertext)
	return ciphertext
#===================================================================

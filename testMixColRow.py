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

def mixColumns(mtrixST): #mix columns in GF(16)
	M = [[1, 2, 6, 4], [2, 1, 4, 6], [6, 4, 1, 2], [4, 6, 2, 1]] 
	newTrix = [[0 for x in range(4)] for y in range(4)] 
	for i in range(0,4):
		for j in range(0,4):
			temp = multiplyGF16(M[i][0],mtrixST[0][j])
			temp2 = multiplyGF16(M[i][1],mtrixST[1][j])
			temp3 = multiplyGF16(M[i][2],mtrixST[2][j])
			temp4 = multiplyGF16(M[i][3],mtrixST[3][j])
			temp = additionGF16(temp,temp2)
			temp = additionGF16(temp,temp3)
			temp = additionGF16(temp,temp4)
			newTrix[i][j] = temp

	return newTrix
  
def mixRows(mtrixST): #mix rows in GF(16)
	M = [[1, 2, 6, 4], [2, 1, 4, 6], [6, 4, 1, 2], [4, 6, 2, 1]] 
	newTrix = [[0 for x in range(4)] for y in range(4)]
	for i in range(0,4):
		for j in range(0,4):
			temp = multiplyGF16(mtrixST[i][0],M[0][j])
			temp2 = multiplyGF16(mtrixST[i][1],M[1][j])
			temp3 = multiplyGF16(mtrixST[i][2],M[2][j])
			temp4 = multiplyGF16(mtrixST[i][3],M[3][j])
			temp = additionGF16(temp,temp2)
			temp = additionGF16(temp,temp3)
			temp = additionGF16(temp,temp4)
			newTrix[i][j] = temp

	return newTrix

A = [[1,2,6,4],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

hasilMixCol = mixColumns(A)
print(hasilMixCol)
hasilMixRow = mixRows(hasilMixCol)
print(hasilMixRow)
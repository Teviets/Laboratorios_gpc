import fakeNumpy as fnp

translate = [[1,0,0,1080/2], [0,1,0,1080/2], [0,0,1,0],[0,0,0,1]]
scale = ([300,0,0,1], [0,300,0,1],[0,0,300,1],[0,0,0,1])

modelmatrix = fnp.timeMatrix(translate,scale)
vertex = [200,200,200,1]

vt = [vertex[0],vertex[1],vertex[2],1]
print(modelmatrix)
print()
print(vt)
temp = fnp.timeMatrixSingle(modelmatrix,vt)
print()
print(temp)
#vt = [temp[0]/temp[3],temp[1]/temp[3],temp[2]/temp[3]]

#print(vt)
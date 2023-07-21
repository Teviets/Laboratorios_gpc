import numpy as np
import fakeNumpy as fnp

matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
matriz2 = [[1,2,3],[4,5,6],[7,8,9]]
matrizsingle = [1,2,3,4]
matrizNp = np.matrix(matriz1)
matrizNp2 = np.matrix(matriz2)
matrizsingleNP = np.matrix(matrizsingle)


#x = matrizNp@matrizsingleNP
print("Numpy: ",matrizNp@matrizNp2)

print("FakeNumpy: ",fnp.timeMatrix(matriz1,matriz2))
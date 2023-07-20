def timeMatrix (matrix1, matrix2):
    result = []

    for alto in range(len(matrix1)):
        result.append([])
        for largo in range(len(matrix1[alto])):
            result[alto].append(0)


    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            result[i][j] = matrix1[i][j] * matrix2[i][j]
            

    return result
        
    
def timeMatrixSingle(matrix1, matrix2):
    filas_matriz = len(matrix1)
    columnas_matriz = len(matrix1[0])
    longitud_vector = len(matrix2)

    if columnas_matriz != longitud_vector:
        raise ValueError("El número de columnas de la matriz debe ser igual a la longitud del vector para calcular el producto punto.")

    resultado = [0] * filas_matriz

    for i in range(filas_matriz):
        for j in range(columnas_matriz):
            resultado[i] += matrix1[i][j] * matrix2[j]

    return resultado

                    



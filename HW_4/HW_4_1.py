matrix = [[1,2], [3 ,4], [5 ,6]]
# trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
# print (trans_matrix)
def trans(array):
    trans_matrix = [[0 for j in range(len(array))] for i in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix

print(matrix)
print(trans(matrix))
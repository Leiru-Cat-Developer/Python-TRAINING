def findTheSafestPath(matrix: list[list[int]]):
    sums = 0
    valuesRows = []
    valueColumns = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sums += matrix[i][j]
        valuesRows.append(sums)
        sums = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            sums += matrix[j][i]
        valueColumns.append(sums)
        sums = 0

    return print(f"\nSafest path has {(min(valuesRows)+min(valueColumns))-1} damage points")

findTheSafestPath([[2,1,5,2],[1,1,1,1],[4,3,5,1],[2,4,6,1],[9,10,11,1],[5,2,7,1]])
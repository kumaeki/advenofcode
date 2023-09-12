def getResult(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()

    result = 0
    matrix = []
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for data in content:
        row = [int(char) for char in data.strip()]
        matrix.append(row)

    l = len(matrix)
    w = len(matrix[0])

    matrix_result = [[-1 for _ in range(w)] for _ in range(l)]

    for i in range(l):
        for j in range(w):
            result += getLowPoint(i, j, moves, matrix, matrix_result) + 1

    return result


def getLowPoint(x, y, moves, matrix, matrix_result):
    if matrix_result[x][y] >= 0:
        return -1

    matrix_result[x][y] = matrix[x][y]
    isMin = True
    for move in moves:
        nextx = x + move[0]
        nexty = y + move[1]
        if nextx < 0 or nextx >= len(matrix) or nexty < 0 or nexty >= len(matrix[0]):
            continue

        if matrix[x][y] < matrix[nextx][nexty]:
            matrix_result[nextx][nexty] = matrix[nextx][nexty]
        elif matrix[x][y] < matrix[nextx][nexty]:
            matrix_result[nextx][nexty] = matrix[nextx][nexty]
            isMin = False
        else:
            isMin = False

    return matrix[x][y] if isMin else -1


result = getResult("./input1.txt")
print("result : {}".format(result))

result = getResult("./input2.txt")
print("result : {}".format(result))
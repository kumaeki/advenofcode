def get_result(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()

    result_list = []
    matrix = []
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for data in content:
        row = [int(char) for char in data.strip()]
        matrix.append(row)

    l = len(matrix)
    w = len(matrix[0])

    matrix_result = [[0 for _ in range(w)] for _ in range(l)]

    for i in range(l):
        for j in range(w):
            temp = getBasinSize(i, j, moves, matrix, matrix_result)
            if temp > 0:
                result_list.append(temp)

    sorted_list = sorted(result_list)
    return sorted_list[-1]*sorted_list[-2]*sorted_list[-3]


def getBasinSize(x, y, moves, matrix, matrix_result):
    if matrix_result[x][y] > 0 or matrix[x][y] == 9:
        return 0

    matrix_result[x][y] = 1
    for move in moves:
        nextx = x + move[0]
        nexty = y + move[1]
        if nextx < 0 or nextx >= len(matrix) or nexty < 0 or nexty >= len(matrix[0]):
            continue

        matrix_result[x][y] += getBasinSize(nextx,
                                            nexty, moves, matrix, matrix_result)

    return matrix_result[x][y]


result = get_result("./input1.txt")
print("result : {}".format(result))

result = get_result("./input2.txt")
print("result : {}".format(result))

import numpy as np


def get_result(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    max_x = 0
    max_y = 0
    fold_lines = []

    for data in content:
        data_strip = data.strip()
        point = data_strip.split(",")
        if len(point) > 1:
            max_x = max(max_x, int(point[0]))
            max_y = max(max_y, int(point[1]))
        elif len(data_strip) > 0:
            fold_line = data_strip.split(" ")[2].split("=")
            fold_lines.append([fold_line[0], int(fold_line[1])])

    matrix = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]

    for data in content:
        data_strip = data.strip()
        point = data_strip.split(",")
        if len(point) > 1:
            matrix[int(point[0])][int(point[1])] = 1

    index = 0
    for fold_line in fold_lines:
        middle = fold_line[1]
        if fold_line[0] == "y":
            for j in range(middle, -1, -1):
                for i in range(max_x + 1):
                    matrix[i][middle - j] |= matrix[i][middle + j]

            max_y = middle - 1
        else:
            for i in range(middle, -1, -1):
                for j in range(max_y + 1):
                    matrix[middle - i][j] |= matrix[middle + i][j]
            max_x = middle - 1
        index += 1

    result_matrix = []

    for i in range(max_x + 1):
        row = []
        for j in range(max_y + 1):
            row.append("#" if matrix[i][j] == 1 else ".")
        result_matrix.append(row)

    matrix_np = np.array(result_matrix)

    np.set_printoptions(linewidth=200)
    print(matrix_np.T)


get_result("./input1.txt")
get_result("./input2.txt")

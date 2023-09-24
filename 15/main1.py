import sys


def get_result(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    matrix = []
    for line in content:
        matrix.append(list(map(int, line.strip())))

    max_x = len(matrix)
    max_y = len(matrix[0])
    pre_row = [0 for _ in range(max_y + 1)]

    first_row = matrix[0]
    for j in range(1, max_y + 1):
        pre_row[j] = pre_row[j - 1] + first_row[j - 1]

    for i in range(1, max_x):
        cur_row = [sys.maxsize for _ in range(max_y + 1)]
        for j in range(1, max_y + 1):
            cur_row[j] = min(cur_row[j - 1], pre_row[j]) + matrix[i][j - 1]
        pre_row = cur_row

    return pre_row[max_y] - matrix[0][0]


print(get_result("./input1.txt"))
print(get_result("./input2.txt"))

import queue
import sys


def get_result(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    # get the origin matrix from input
    matrix_origin = []
    for line in content:
        matrix_origin.append(list(map(int, line.strip())))

    # extend the columns
    matrix_with_whole_row = []
    for row in matrix_origin:
        matrix_with_whole_row.append(get_whole_row(row))

    # extend the rows, get the whole matrix
    h = len(matrix_with_whole_row)
    new_h = h * 5
    l = len(matrix_with_whole_row[0])
    matrix = []
    for i in range(0, new_h):
        times = i // h
        mod = i % h
        matrix.append(get_next_row(matrix_with_whole_row[mod], times))

    # dfs, but not recursive
    matrix_visited = [[sys.maxsize for _ in range(l)] for _ in range(new_h)]
    matrix_visited[0][0] = 0
    moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    que = queue.Queue()
    que.put([0, 0])
    total = 0
    while not que.empty():
        current = que.get()

        for move in moves:
            new_x = current[0] + move[0]
            new_y = current[1] + move[1]
            if new_x < 0 or new_x >= new_h or new_y < 0 or new_y >= l:
                continue
            total = matrix_visited[current[0]][current[1]]
            total += matrix[new_x][new_y]
            if total >= matrix_visited[new_x][new_y]:
                continue

            matrix_visited[new_x][new_y] = total
            que.put([new_x, new_y])

    return matrix_visited[new_h - 1][l - 1]


def get_whole_row(row):
    result_row = []
    for i in range(5):
        for item in row:
            new_item = item + i
            result_row.append(new_item if new_item < 10 else new_item - 9)
    return result_row


def get_next_row(row, times):
    result_row = []
    for item in row:
        new_item = item + times
        result_row.append(new_item if new_item < 10 else new_item - 9)
    return result_row


print(get_result("./input1.txt"))
print(get_result("./input2.txt"))

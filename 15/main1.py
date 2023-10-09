import queue
import sys


def get_result(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    matrix = []
    for line in content:
        matrix.append(list(map(int, line.strip())))

    # dfs, but not recursive
    h = len(matrix)
    l = len(matrix[0])
    matrix_visited = [[sys.maxsize for _ in range(l)] for _ in range(h)]
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
            if new_x < 0 or new_x >= h or new_y < 0 or new_y >= l:
                continue
            total = matrix_visited[current[0]][current[1]]
            total += matrix[new_x][new_y]
            if total >= matrix_visited[new_x][new_y]:
                continue

            matrix_visited[new_x][new_y] = total
            que.put([new_x, new_y])

    return matrix_visited[h - 1][l - 1]


print(get_result("./input1.txt"))
print(get_result("./input2.txt"))

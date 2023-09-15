def get_result(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    matrix = []
    result = 0
    moves = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

    for data in content:
        row = [int(char) for char in data.strip()]
        matrix.append(row)

    length = len(matrix)
    width = len(matrix[0])
    max = length * width

    for i in range(99999):
        flash_count = 0
        for x in range(length):
            for y in range(width):
                flash_count += sub_func(x, y, matrix, moves)

        if flash_count == max:
            result = i
            break

        for x in range(length):
            for y in range(width):
                if matrix[x][y] == -1:
                    matrix[x][y] = 0
    return result + 1


def sub_func(x, y, matrix, moves):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return 0

    if matrix[x][y] == -1:
        return 0

    if matrix[x][y] == 9:
        matrix[x][y] = -1
        result = 1
        for move in moves:
            result += sub_func(x + move[0], y + move[1], matrix, moves)
        return result

    matrix[x][y] += 1
    return 0


print(get_result("./input1.txt"))
print(get_result("./input2.txt"))

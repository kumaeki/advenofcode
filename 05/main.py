def getPoints(line):
    point1, point2 = line.split(" -> ")
    x1, y1 = point1.split(",")
    x2, y2 = point2.split(",")
    return int(x1), int(y1), int(x2), int(y2)


def getAmountOfPoints(file_path):
    result = 0

    with open(file_path, "r") as file:
        content = file.readlines()

    maxX = 0
    maxY = 0
    # remove the useless data
    new_matrix = []
    for line in content:
        x1, y1, x2, y2 = getPoints(line.strip())
        if x1 != x2 and y1 != y2 and abs(x1 - x2) != abs(y1 - y2):
            continue
        maxX = max(maxX, x1, x2)
        maxY = max(maxY, y1, y2)
        new_matrix.append([x1, y1, x2, y2])

    # define the matrix for compute
    rows = maxX + 1
    cols = maxY + 1
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # start to compute
    for data in new_matrix:
        x1 = data[0]
        y1 = data[1]
        x2 = data[2]
        y2 = data[3]
        # horizontal
        if x1 == x2:
            smallY = min(y1, y2)
            bigY = max(y1, y2)
            for i in range(smallY, bigY + 1):
                if matrix[x1][i] == 0:
                    matrix[x1][i] = 1
                elif matrix[x1][i] == 1:
                    matrix[x1][i] = 2
                    result = result + 1
        # vertical
        elif y1 == y2:
            smallX = min(x1, x2)
            bigX = max(x1, x2)
            for i in range(smallX, bigX + 1):
                if matrix[i][y1] == 0:
                    matrix[i][y1] = 1
                elif matrix[i][y1] == 1:
                    matrix[i][y1] = 2
                    result = result + 1
        # diagonal
        else:
            stepX = 1 if x1 < x2 else -1
            stepY = 1 if y1 < y2 else -1
            tempX = x1
            tempY = y1
            while tempX != x2 + stepX:
                if matrix[tempX][tempY] == 0:
                    matrix[tempX][tempY] = 1
                elif matrix[tempX][tempY] == 1:
                    matrix[tempX][tempY] = 2
                    result = result + 1
                tempX = tempX + stepX
                tempY = tempY + stepY
    return result


result = getAmountOfPoints("input.txt")
print("result : {}".format(result))

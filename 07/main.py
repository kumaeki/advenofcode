import sys


def getLeastFuel(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()
    data = content[0].split(",")
    data_int = list(map(int, data))
    maxItem = max(data_int)
    result = sys.maxsize
    for i in range(maxItem):
        currentFule = 0
        for item in data_int:
            currentFule += abs(item - i)
        result = min(result, currentFule)

    return result


result = getLeastFuel("input1.txt")
print("result : {}".format(result))

result = getLeastFuel("input2.txt")
print("result : {}".format(result))


def getFuelBySteps(steps):
    return steps * (steps + 1) / 2


def getLeastFuel_v2(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()
    data = content[0].split(",")
    data_int = list(map(int, data))
    maxItem = max(data_int)
    result = sys.maxsize
    for i in range(maxItem):
        currentFule = 0
        for item in data_int:
            currentFule += getFuelBySteps(abs(item - i))
        result = min(result, currentFule)

    return result


result = getLeastFuel_v2("input1.txt")
print("result : {}".format(result))

result = getLeastFuel_v2("input2.txt")
print("result : {}".format(result))

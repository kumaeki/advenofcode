def getCountOfUniqueDigits(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()

    result = 0
    for data in content:
        outputs = data.split("|")[1].strip().split(" ")
        for output in outputs:
            if len(output) in [2, 3, 4, 7]:
                result += 1

    return result


result = getCountOfUniqueDigits("input1.txt")
print("result : {}".format(result))

result = getCountOfUniqueDigits("input2.txt")
print("result : {}".format(result))


def getSum(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()

    result = 0
    for data in content:
        list = [[] for _ in range(9)]
        dict = {}
        inputs = data.split("|")[0].strip().split(" ")
        outputs = data.split("|")[1].strip().split(" ")

        for item in inputs:
            list[len(item)].append(set(item))

        dict[1] = list[2][0]

        dict[4] = list[4][0]

        dict[7] = list[3][0]

        dict[8] = list[7][0]

        a = dict[7].difference(dict[1])
        abcdf = a.union(dict[4])
        for temp in list[6]:
            set_temp = temp.difference(abcdf)
            if len(set_temp) > 0:
                g = set_temp
                dict[9] = temp
                list[6].remove(temp)
                break
        e = dict[8].difference(dict[9])

        for temp in list[5]:
            if dict[1].issubset(temp):
                dict[3] = temp
                list[5].remove(temp)
                break

        for temp in list[5]:
            if e.issubset(temp):
                dict[2] = temp
                list[5].remove(temp)
                break

        dict[5] = list[5][0]

        c = dict[9].difference(dict[5])

        for temp in list[6]:
            if c.issubset(temp):
                dict[0] = temp
                list[6].remove(temp)
                break

        dict[6] = list[6][0]

    return result


result = getSum("input1.txt")
print("result : {}".format(result))

# result = getSum("input2.txt")
# print("result : {}".format(result))

def getResult_q1(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()

    result = 0
    for data in content:
        outputs = data.split("|")[1].strip().split(" ")
        for output in outputs:
            if len(output) in [2, 3, 4, 7]:
                result += 1

    return result


result = getResult_q1("./input1.txt")
print("result : {}".format(result))

result = getResult_q1("./input2.txt")
print("result : {}".format(result))

result = getResult_q1("./input3.txt")
print("result : {}".format(result))


def getResult_q2(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()

    result = 0
    for data in content:
        list = [[] for _ in range(9)]
        dict = {}
        list_result = []
        inputs = data.split("|")[0].strip().split(" ")
        outputs = data.split("|")[1].strip().split(" ")

        for item in inputs:
            list[len(item)].append(set(item))

        dict[1] = list[2][0]

        dict[4] = list[4][0]

        dict[7] = list[3][0]

        dict[8] = list[7][0]

        a = dict[7] - dict[1]
        abcdf = a.union(dict[4])
        for temp in list[6]:
            if len(temp - abcdf) == 1:
                dict[9] = temp
                list[6].remove(temp)
                break
        e = dict[8] - dict[9]

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

        c = dict[9] - dict[5]

        for temp in list[6]:
            if c.issubset(temp):
                dict[0] = temp
                list[6].remove(temp)
                break

        dict[6] = list[6][0]

        for output in outputs:
            output_set = set(output)
            for k, v in dict.items():
                if v == output_set:
                    list_result.append(k)

        result += (
            list_result[0] * 1000
            + list_result[1] * 100
            + list_result[2] * 10
            + list_result[3]
        )

    return result


result = getResult_q2("./input1.txt")
print("result : {}".format(result))

result = getResult_q2("./input2.txt")
print("result : {}".format(result))

result = getResult_q2("./input3.txt")
print("result : {}".format(result))

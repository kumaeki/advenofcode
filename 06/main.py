# recursion
# def getAmout(start, days):
#     if(days <= start):
#         return 1
#     return getAmout(6, days - start - 1) + getAmout(8, days - start - 1)



# closed-form solution
def getAmout(start, days):
    n = days - start - 1
    if n <= 0:
        return 1

    return (2 ** (n // 8)  + 1) * (2 ** ((n % 8) // 6) )

def getAmountOfPoints(file_path, days):
    result = 0

    with open(file_path, "r") as file:
        content = file.readlines()

    list = content[0].split(',')

    for item in list:
        it = int(item)
        result = result + getAmout(it, days)
        # print("result : {}".format(result))

    print(list)
    return result


result = getAmountOfPoints("input.txt", 18)
print("result : {}".format(result))

result = getAmountOfPoints("input.txt", 80)
print("result : {}".format(result))

result = getAmountOfPoints("input.txt", 256)
print("result : {}".format(result))

result = getAmountOfPoints("input.txt.test2", 80)
print("result : {}".format(result))

result = getAmountOfPoints("input.txt.test2", 256)
print("result : {}".format(result))

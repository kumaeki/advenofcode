# recursion
# def getAmout(start, days):
#     if(days <= start):
#         return 1
#     return getAmout(6, days - start - 1) + getAmout(8, days - start - 1)

# def getAmountOfPoints(file_path, days):
#     result = 0
#     with open(file_path, "r") as file:
#         content = file.readlines()
#     data = content[0].split(',')
#     for item in data:
#         it = int(item)
#         result = result + getAmout(it, days)
#     return result

def getAmountOfPoints(file_path, days):
    with open(file_path, "r") as file:
        content = file.readlines()
    data = content[0].split(',')
    array = [data.count(str(i)) for i in range(9)]
    for i in range(days):
        num = array.pop(0)
        array[6] += num
        array.append(num)

    return sum(array)

result = getAmountOfPoints("input.txt", 18)
print("result : {}".format(result))
result = getAmountOfPoints("input.txt", 80)
print("result : {}".format(result))
result = getAmountOfPoints("input.txt.test2", 80)
print("result : {}".format(result))
result = getAmountOfPoints("input.txt", 256)
print("result : {}".format(result))
result = getAmountOfPoints("input.txt.test2", 256)
print("result : {}".format(result))

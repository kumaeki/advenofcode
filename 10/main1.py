def get_result(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    result = 0
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    times = {")": 0, "]": 0, "}": 0, ">": 0}
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}

    for data in content:
        row = [char for char in data.strip()]
        sub_func(row, times,pairs)       

    for item in points.keys():
        result += points[item]*times[item]

    return result


def sub_func(data,times,pairs):
    new_data = []
    for item in data:

        if  item not in pairs:
            new_data.append(item)
            continue

        pair = pairs[item]
        size = len(new_data)

        if new_data[size - 1] == pair:
            new_data.pop()
        else:
            times[item] += 1
            break

print(get_result("./input1.txt"))
print(get_result("./input2.txt"))

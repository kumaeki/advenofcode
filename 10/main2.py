def get_result(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    result = 0
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    point_list = []
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    pairs_left = {"(": ")", "[": "]", "{": "}", "<": ">"}

    for data in content:
        point = 0
        row = [char for char in data.strip()]
        isCorrupted, new_row = sub_func(row, pairs)
        if not isCorrupted and len(new_row) > 0:
            for i in range(len(new_row) - 1, -1, -1):
                item = new_row[i]
                pair = pairs_left[item]
                point = point * 5 + points[pair]
            point_list.append(point)

    index = len(point_list) // 2
    point_list.sort()

    return point_list[index]


def sub_func(data, pairs):
    new_data = []
    for item in data:
        if item not in pairs:
            new_data.append(item)
            continue

        pair = pairs[item]
        size = len(new_data)

        if new_data[size - 1] == pair:
            new_data.pop()
        else:
            return True, new_data
    return False, new_data


print(get_result("./input1.txt"))
print(get_result("./input2.txt"))

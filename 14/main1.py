import sys


def get_result(file_path, steps):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    start = content[0].strip()
    rules = {}
    linked_list = {}
    result_string = start[0]
    quantities = {}
    quantity_min = sys.maxsize
    quntity_max = -1

    for i in range(2, len(content)):
        data = content[i].strip().split("->")
        rules[data[0].strip()] = data[1].strip()

    for key, value in rules.items():
        linked_list[key] = [key[0] + value, value + key[1]]

    for i in range(len(start) - 1):
        start_two_char = start[i : i + 2]
        result_string += get_string(start_two_char, linked_list, steps)[1:]

    for c in result_string:
        if c in quantities:
            quantities[c] += 1
        else:
            quantities[c] = 1

    time_values = quantities.values()
    quantity_min = min(time_values)
    quntity_max = max(time_values)

    return quntity_max - quantity_min


def get_string(start, linked_list, steps):
    if steps == 0:
        return start

    next = linked_list[start]

    left = get_string(next[0], linked_list, steps - 1)
    right = get_string(next[1], linked_list, steps - 1)

    return left + right[1:]


print(get_result("./input1.txt", 10))
print(get_result("./input2.txt", 10))
print(get_result("./input2.txt", 40))

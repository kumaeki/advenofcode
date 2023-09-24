from collections import Counter


def get_result(file_path, steps):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    start = content[0].strip()
    quantities_char = Counter(start)
    # NNCB -> {'NN' : 1 , 'NC' : 1 , 'CB' : 1}
    quantities_sting = Counter(map(str.__add__, start, start[1:]))

    rules_origin = map(str.strip, content[2:])
    rules = dict(row.split(" -> ") for row in rules_origin)

    for i in range(steps):
        for (left, right), count in quantities_sting.copy().items():
            next = rules[left + right]

            quantities_sting[left + right] -= count
            increment_quantity(left + next, quantities_sting, count)
            increment_quantity(next + right, quantities_sting, count)

            increment_quantity(next, quantities_char, count)

    time_values = quantities_char.values()
    return max(time_values) - min(time_values)


def increment_quantity(current, quantities, count):
    if current in quantities:
        quantities[current] += count
    else:
        quantities[current] = count


print(get_result("./input1.txt", 10))
print(get_result("./input2.txt", 10))
print(get_result("./input1.txt", 40))
print(get_result("./input2.txt", 40))

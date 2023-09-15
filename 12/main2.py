def get_result(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    dict = {}
    times = {}
    is_twice = False

    for data in content:
        nodes = data.strip().split("-")
        n1 = nodes[0]
        n2 = nodes[1]
        insert_node_to_dict(n1, n2, dict, times)
        insert_node_to_dict(n2, n1, dict, times)

    node_list = ["start"]
    result = sub_func("start", dict, times, node_list, is_twice)

    return result


def insert_node_to_dict(n1, n2, dict, times):
    if n1 == "end" or n2 == "start":
        return
    if n1.islower():
        times[n1] = 0
    if n1 in dict:
        dict[n1].append(n2)
    else:
        dict[n1] = [n2]


def sub_func(current_node, dict, times, node_list, is_twice):
    if current_node == "end":
        return 1

    if current_node != "start" and current_node.islower():
        if times[current_node] > 1 or (is_twice and times[current_node] > 0):
            return 0
        else:
            times[current_node] += 1
            if times[current_node] > 1:
                is_twice = True

    result = 0
    for node in dict[current_node]:
        node_list.append(node)
        result += sub_func(node, dict, times, node_list, is_twice)
        node_list.pop()

    if current_node != "start" and current_node.islower():
        times[current_node] -= 1
        if times[current_node] == 1:
            is_twice = False

    return result


print(get_result("./input1.txt"))
print(get_result("./input2.txt"))
print(get_result("./input3.txt"))
print(get_result("./input4.txt"))

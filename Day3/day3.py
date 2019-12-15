from time import time


def read_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines


def get_manhattan_distance(inter_set):
    distance_list = []
    for z in inter_set:
        dist = int(abs(int(z.split(",")[0]))) + int(abs(int(z.split(",")[1])))
        distance_list.append(dist)
    distance_list.sort()
    return distance_list


def wire_step_path(x, top, right, target):
    cords_to_add = []
    step = 0
    for y in range(0, int(x[1:])):
        if x[:1] == 'R':
            right += 1  # Right
        elif x[:1] == 'L':
            right -= 1  # Left
        elif x[:1] == 'U':
            top += 1  # Up
        elif x[:1] == 'D':
            top -= 1  # Down
        current_cord = str(top) + "," + str(right)
        if target != 0 and target == current_cord:
            return cords_to_add, top, right, step
        step += 1
        cords_to_add.append(current_cord)
    return cords_to_add, top, right, step


def create_map_to_target(wire, target):
    top = 0
    right = 0
    steps = 0
    for x in wire:
        add_cords, top, right, step_done = wire_step_path(x, top, right, target)
        if top == target.split(",")[0] and right == target.split(",")[1]:
            return steps
        steps += step_done
    return steps


def create_map(wire):
    wire_set = set()
    top = 0
    right = 0
    for x in wire:
        add_cords, top, right, step_done = wire_step_path(x, top, right, 0)
        wire_set.update(add_cords)
    return wire_set


def get_distance_for_wires(x, wire_a, wire_b):
    return create_map_to_target(wire_a, x) + create_map_to_target(wire_b, x)


def function_a():
    start = time()
    pointer = 0
    for wire in read_file("input.txt"):
        if pointer == 0:
            wire_a = wire.split(",")
        else:
            wire_b = wire.split(",")
        pointer += 1
    return get_manhattan_distance(create_map(wire_a).intersection(create_map(wire_b)))[0], time()-start


def function_b():
    start = time()
    pointer = 0
    for wire in read_file("input.txt"):
        if pointer == 0:
            wire_a = wire.split(",")
        else:
            wire_b = wire.split(",")
        pointer += 1
    inter = create_map(wire_a).intersection(create_map(wire_b))
    distance_list = []
    for x in inter:
        distance_list.append(get_distance_for_wires(x, wire_a, wire_b))
    distance_list.sort()
    return distance_list[0], time()-start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Closest distance: {}. Completed in {}.".format(resultA, timeA))
    resultB, timeB = function_b()
    print("Closest route to intersection: {}. Completed in {}.".format(resultB, timeB))


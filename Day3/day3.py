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
    return distance_list


def create_map(wire):
    wire_set = set()
    top = 0
    right = 0
    for x in wire:
        cords_to_add = []
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
            cords_to_add.append(current_cord)
        wire_set.update(cords_to_add)
    return wire_set


def function_a():
    start = time()
    pointer = 0
    for wire in read_file("input.txt"):
        if pointer == 0:
            wire_a = wire.split(",")
        else:
            wire_b = wire.split(",")
        pointer += 1
    a_cords = create_map(wire_a)
    b_cords = create_map(wire_b)
    distance = get_manhattan_distance(a_cords.intersection(b_cords))
    smallest_distance = distance[0]
    for x in distance:
        if x < smallest_distance:
            smallest_distance = x
    return smallest_distance, time()-start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Closest distance: {}. Completed in {}.".format(resultA, timeA))

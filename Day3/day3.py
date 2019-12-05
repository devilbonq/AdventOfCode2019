from time import time


def read_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines


def coordinates_decoder(wire):
    print(wire)
    wire[1:]
    top = 0
    right =0
    for x in wire:
        prev_top = top
        prev_right = right
        if x[:1] == 'R':
            right += int(x[1:])
        elif x[:1] == 'L':
            right -= int(x[1:])
        elif x[:1] == 'U':
            top += int(x[1:])
        elif x[:1] == 'D':
            top -= int(x[1:])
    return '1,1', '2,1'


def map_coordinates(wire):
    cords = map(coordinates_decoder, wire)
    print(set(cords))
    return cords


def construct_coordinates(wire):
    cord_dict = {}
    right = 0
    top = 0
    pointer = 0
    for x in wire:
        prev_top = top
        prev_right = right
        if x[:1] == 'R':
            right += int(x[1:])
        elif x[:1] == 'L':
            right -= int(x[1:])
        elif x[:1] == 'U':
            top += int(x[1:])
        elif x[:1] == 'D':
            top -= int(x[1:])
        top_change = top - prev_top
        right_change = right - prev_right
        if top_change != 0:
            if top_change > 0:
                for z in range(0, abs(top_change)):
                    cord_dict.__setitem__('step' + str(pointer), str(prev_top + z) + ',' + str(right))
                    pointer += 1
            else:
                for z in range(0, abs(top_change)):
                    cord_dict.__setitem__('step' + str(pointer), str(prev_top - z) + ',' + str(right))
                    pointer += 1
        else:
            if right_change > 0:
                for z in range(0, abs(right_change)):
                    cord_dict.__setitem__('step' + str(pointer), str(top) + ',' + str(prev_right + z))
                    pointer += 1
            else:
                for z in range(0, abs(right_change)):
                    cord_dict.__setitem__('step' + str(pointer), str(top) + ',' + str(prev_right - z))
                    pointer += 1
    return flip_dictionary_key_value(cord_dict)


def flip_dictionary_key_value(d):
    flipped_dict = {}
    for key, value in d.items():
        if value not in flipped_dict:
            flipped_dict[value] = [key]
        else:
            flipped_dict[value].append(key)
    return flipped_dict


def get_intersection(dict_a, dict_b):
    intersection_list = []
    dict_a_set = set(dict_a)
    dict_b_set = set(dict_b)
    if len(dict_a) > len(dict_b):
        for cord in dict_a_set.intersection(dict_b_set):
            intersection_list.append(cord)
    else:
        for cord in dict_b_set.intersection(dict_a_set):
            intersection_list.append(cord)
    return intersection_list


def get_manhattan_distance(distance):
    y = int(distance.split(",")[0])
    x = int(distance.split(",")[1])
    return abs(y) + abs(x)


def function_a():
    start = time()
    pointer = 0
    for wire in read_file("input.txt"):
        if pointer == 0:
            wire_a = wire.split(",")
        else:
            wire_b = wire.split(",")
        pointer += 1
    wire_a_dict = construct_coordinates(wire_a)
    wire_b_dict = construct_coordinates(wire_b)
    map_coordinates(wire_a)
    distance_list = []
    for intersect in get_intersection(wire_a_dict, wire_b_dict):
        distance_list.append(get_manhattan_distance(intersect))
    distance_list.sort()
    return distance_list[0], time()-start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Closest distance: {}. Completed in {}.".format(resultA, timeA))

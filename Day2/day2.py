from time import time


def read_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines


def function_a():
    start = time()
    input_file = read_file("input.txt")
    optcode_list = input_file[0].split(",")
    pointer = 0
    while pointer < len(optcode_list) and int(optcode_list[pointer]) != 99:
        if int(optcode_list[pointer]) == 1:
            optcode_list[int(optcode_list[pointer+3])] = int(optcode_list[int(optcode_list[pointer+1])]) + int(optcode_list[int(optcode_list[pointer+2])])
        elif int(optcode_list[pointer]) == 2:
            optcode_list[int(optcode_list[pointer + 3])] = int(optcode_list[int(optcode_list[pointer + 1])]) * int(optcode_list[int(optcode_list[pointer + 2])])
        pointer += 4
    return optcode_list[0], time()-start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Optcode value: {}. Completed in {}.".format(resultA, timeA))
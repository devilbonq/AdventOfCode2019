from time import time


def read_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines


def optcode_runtime(optcode, optcode_list, pointer):
    if optcode == 1:
        optcode_list[int(optcode_list[pointer + 3])] = int(optcode_list[int(optcode_list[pointer + 1])]) + int(
            optcode_list[int(optcode_list[pointer + 2])])
    elif optcode == 2:
        optcode_list[int(optcode_list[pointer + 3])] = int(optcode_list[int(optcode_list[pointer + 1])]) * int(
            optcode_list[int(optcode_list[pointer + 2])])
    return optcode_list


def analyze_optcode(optcode_list):
    pointer = 0
    while pointer < len(optcode_list) and int(optcode_list[pointer]) != 99:
        if int(optcode_list[pointer]) == 1:
            optcode_list = optcode_runtime(1, optcode_list, pointer)
        elif int(optcode_list[pointer]) == 2:
            optcode_list = optcode_runtime(2, optcode_list, pointer)
        pointer += 4
    return int(optcode_list[0])


def function_a():
    start = time()
    input_file = read_file("input.txt")
    optcode_list = input_file[0].split(",")
    return analyze_optcode(optcode_list), time()-start


def function_b():
    start = time()
    input_file = read_file("input.txt")
    optcode_list = input_file[0].split(",")
    pointer = 0
    noun = 0
    verb = 0

    while int(optcode_list[0]) != 19690720 and int(optcode_list[pointer]) != 99:
        verb = 0
        while verb < 99 and int(optcode_list[pointer]) != 99:
            input_file = read_file("input.txt")
            optcode_list = input_file[0].split(",")
            optcode_list[1] = noun
            optcode_list[2] = verb
            if analyze_optcode(optcode_list) == 19690720:
                return noun, verb, time() - start
            elif verb == 99:
                break
            else:
                verb += 1
                pointer = 0
        noun += 1
        pointer = 0
        if noun > 99:
            return 0, 0, time()-start
    return noun, verb, time()-start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Optcode value: {}. Completed in {}.".format(resultA, timeA))
    resultB1, resultB2, timeB = function_b()
    print("Noun: {} Verb: {} Answer: {}. Completed in {}.".format(resultB1, resultB2, 100*int(resultB1)+int(resultB2),
                                                                  timeB))

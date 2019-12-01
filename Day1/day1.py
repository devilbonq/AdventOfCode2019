from time import time
import math


def read_file(inputFile):
    with open(inputFile, "r") as f:
        lines = f.readlines()
    return lines


def function_a():
    start = time()
    fuel_req = 0
    for x in read_file("input.txt"):
        fuel_req += math.floor(int(x)/3) - 2
    return fuel_req, time() - start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Fuel requirement: {}. Completed in {}.".format(resultA, timeA))

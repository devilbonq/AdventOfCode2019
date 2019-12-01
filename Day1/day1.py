from time import time
from math import floor


def read_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines


def get_fuel_req(mass):
    return floor(int(mass)/3) - 2


def function_a():
    start = time()
    fuel_req = 0
    for mass in read_file("input.txt"):
        fuel_req += get_fuel_req(mass)
    return fuel_req, time() - start


def function_b():
    start = time()
    fuel_req = 0

    for mass in read_file("input.txt"):
        module_mass_fuel_req = get_fuel_req(mass)
        additional_fuel_cost = get_fuel_req(module_mass_fuel_req)
        while additional_fuel_cost > 0:
            prev_mass = module_mass_fuel_req
            module_mass_fuel_req = module_mass_fuel_req + additional_fuel_cost
            additional_fuel_cost = get_fuel_req(module_mass_fuel_req - prev_mass)
        fuel_req += module_mass_fuel_req
    return fuel_req, time() - start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Fuel requirement: {}. Completed in {}.".format(resultA, timeA))
    resultB, timeB = function_b()
    print("Fuel requirement: {}. Completed in {}.".format(resultB, timeB))

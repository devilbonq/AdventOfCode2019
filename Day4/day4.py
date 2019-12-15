from time import time


def read_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines


def get_range(line):
    return int(line.split("-")[0]), int(line.split("-")[1])


def validate_number_not_descending(password):
    password_meet_criteria = True
    for iterator in range(0, 5):
        if int(str(password)[iterator]) > int(str(password)[iterator + 1]):
            password_meet_criteria = False
            break
    return password_meet_criteria


def validate_digit_repeat(password):
    repeated_twice = False
    for element in list(set(password)):
        if password.count(element) == 2:
            repeated_twice = True
            break
    return repeated_twice


def function_a():
    start = time()
    range_min, range_max = get_range(read_file("input.txt")[0])
    passwords_counter = 0
    for password in range(range_min, range_max):
        password_meet_criteria = False
        for iterator in range(0, 5):
            if str(password)[iterator] == str(password)[iterator+1]:
                password_meet_criteria = True
        if password_meet_criteria:
            passwords_counter += validate_number_not_descending(password)
    return passwords_counter, time() - start


def function_b():
    start = time()
    passwords_counter = 0
    range_min, range_max = get_range(read_file("input.txt")[0])
    for password in range(range_min, range_max):
        if validate_digit_repeat(str(password)):
            passwords_counter += validate_number_not_descending(password)
    return passwords_counter, time() - start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Passwords that meet criteria: {}. Completed in {}.".format(resultA, timeA))
    resultB, timeB = function_b()
    print("Passwords that meet criteria: {}. Completed in {}.".format(resultB, timeB))
from time import time


def read_file(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    return lines


def get_range(line):
    return int(line.split("-")[0]), int(line.split("-")[1])


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
            for iterator in range(0, 5):
                if password_meet_criteria and int(str(password)[iterator]) > int(str(password)[iterator+1]):
                    password_meet_criteria = False
                    break
        if password_meet_criteria:
            passwords_counter += 1

    return passwords_counter, time() - start


if __name__ == '__main__':
    resultA, timeA = function_a()
    print("Passwords that meet criteria: {}. Completed in {}.".format(resultA, timeA))
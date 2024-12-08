# For example, consider the following section of corrupted memory:
#
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces
# 161 (2*4 + 5*5 + 11*8 + 8*5).
#
# Scan the corrupted memory for uncorrupted mul instructions.
# What do you get if you add up all of the results of the multiplications?

import regex


def find_functions_in_file(file):
    with open(file) as f:
        file_result = []
        for line in f.readlines():
            file_result.append(
                find_functions(line)
            )
    return file_result


def find_functions(memory):
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    multiplication_results = []
    for multiplication in regex.findall(pattern, memory):
        multiplication_results.append(
            multiply(multiplication.split(","))
        )
    return multiplication_results


def multiply(list_of_two):
    return int(list_of_two[0]) * int(list_of_two[1])


test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test_file = "3.multiplication-long.txt"

results = find_functions(test_string)
print(results)
print(f"Grand total: {sum(results)}\n")

file_results = find_functions_in_file(test_file)
line_sums = []
for result in file_results:
    line_sums.append(sum(result))

print(line_sums)
print(f"Grand total: {sum(line_sums)}\n")

# There are two new instructions you'll need to handle:
#
# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies.
# At the beginning of the program, mul instructions are enabled.


def find_enabled_functions_in_file(file):
    with open(file) as f:
        dos = []
        for line in f.readlines():
            for item in line.split("do()"):
                dos.append(item.split("don't()")[0])
    return dos


def find_enabled_functions_in_string(memory_string):
    dos = []
    for item in memory_string.split("do()"):
        dos.append(item.split("don't()")[0])
    return dos


def find_functions_in_list(functions_list):
    result_list = []
    for item in functions_list:
        result_list.append(find_functions(item))
    return result_list


test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
results_list = find_enabled_functions_in_string(test_string)
results_list = find_functions_in_list(results_list)
results_list = [sum(result) for result in results_list]
print(results_list)
print(f"Grand total: {sum(results_list)}\n")

valid_functions = find_enabled_functions_in_file(test_file)
results_list = find_functions_in_list(valid_functions)
print(results_list)

results_list = [sum(mul_list) for mul_list in results_list]
print(results_list)
print(f"Grand total: {sum(results_list)}\n")

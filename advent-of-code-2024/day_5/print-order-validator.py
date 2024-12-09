from printer_tasks import print_tasks
from rules import rules_list

# rules_list = [
#     [47, 53], [97, 13], [97, 61], [97, 47], [75, 29], [61, 13], [75, 53], [29, 13], [97, 29], [53, 29], [61, 53],
#     [97, 53], [61, 29], [47, 13], [75, 47], [97, 75], [47, 61], [75, 61], [47, 29], [75, 13], [53, 13]
# ]
# print_tasks = [
#     [75, 47, 61, 53, 29],
#     [97, 61, 53, 29, 13],
#     [75, 29, 13],
#     [75, 97, 47, 61, 53],
#     [61, 13, 29],
#     [97, 13, 75, 29, 47]
# ]


def validate_task(rules_list_, print_task_):
    for rule in rules_list_:
        if rule[0] in print_task_ and rule[1] in print_task_:
            if print_task_.index(rule[0]) > print_task_.index(rule[1]):
                return False
    return True


def fix_task(rules_list_, print_task_: list, iteration=0):
    if isinstance(iteration, int) and iteration > len(print_task_):
        return None
    for rule in rules_list_:
        if rule[0] in print_task_ and rule[1] in print_task_:
            if print_task_.index(rule[0]) > print_task_.index(rule[1]):
                moved_item = print_task_.pop(
                    print_task_.index(rule[1])
                )
                print_task_.append(moved_item)
                fix_task(rules_list_, print_task_, iteration=iteration + 1)
    return print_task_


middle_pages = []
invalid_print_tasks = []
for print_task in print_tasks:
    validation_status = validate_task(rules_list, print_task)
    print(f"{print_task} - {validation_status}")
    if validation_status:
        middle_index = int(len(print_task) / 2)
        middle_pages.append(print_task[middle_index])
    else:
        invalid_print_tasks.append(print_task)

print()
print(f"Middle pages: {middle_pages}")
print(f"Middle pages sum: {sum(middle_pages)}")

print()
print(f"Invalid tasks: {invalid_print_tasks}")

middle_pages = []
revalidated_print_tasks = []
for print_task in invalid_print_tasks:
    revalidated_print_tasks.append(
        fix_task(rules_list, print_task)
    )
    middle_index = int(len(print_task) / 2)
    middle_pages.append(print_task[middle_index])

print(f"Validated tasks: {revalidated_print_tasks}")
print()
print(f"Middle pages: {middle_pages}")
print(f"Middle pages sum: {sum(middle_pages)}")


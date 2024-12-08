'''
The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe.
 The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually
 decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
'''
reports_list = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]


def validate_report(report):
    if report[0] > report[1]:
        i = 1
        for measure in report:
            if i == len(report):
                break
            if measure < report[i]:
                return False
            if not 1 <= measure - report[i] <= 3:
                return False
            i = i + 1

    elif report[0] < report[1]:
        i = 1
        for measure in report:
            if i == len(report):
                break
            if measure > report[i]:
                return False
            if not 1 <= report[i] - measure <= 3:
                return False
            i = i + 1
    else:
        return False

    return True


def check_reports(list_reports):
    check_results = []
    for report in list_reports:
        check_results.append({
            "Report": report,
            "Validation": validate_report(report)
        })
    return check_results


print(check_reports(reports_list))



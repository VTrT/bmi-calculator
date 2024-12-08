"""
The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers
called levels that are separated by spaces. For example:

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
"""


def validate_report(report, problem_dampener_enabled: bool, org_len: int):
    if len(report) != org_len - 1 and len(report) != org_len:
        return False
    if report[0] > report[1]:
        i = 1
        for measure in report:
            if i == len(report):
                break
            if measure < report[i]:
                if problem_dampener_enabled:
                    report.pop(i - 1)
                    return validate_report(report, True, org_len)
                else:
                    return False
            if not 1 <= measure - report[i] <= 3:
                if problem_dampener_enabled:
                    report.pop(i - 1)
                    return validate_report(report, True, org_len)
                else:
                    return False
            i = i + 1
    elif report[0] < report[1]:
        i = 1
        for measure in report:
            if i == len(report):
                break
            if measure > report[i]:
                if problem_dampener_enabled:
                    report.pop(i - 1)
                    return validate_report(report, True, org_len)
                else:
                    return False
            if not 1 <= report[i] - measure <= 3:
                if problem_dampener_enabled:
                    report.pop(i - 1)
                    return validate_report(report, True, org_len)
                else:
                    return False
            i = i + 1
    else:
        return False
    return True


def check_reports(list_reports, problem_dampener_enabled: bool):
    check_results = []
    for report in list_reports:
        check_results.append({
            "Report": report,
            "Validation": validate_report(report, problem_dampener_enabled, len(report))
        })
    return check_results


def pretty_report(list_reports):
    for report in list_reports:
        print(f"{report['Report']} - {report["Validation"]}")


reports_list = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]
validated_reports_list = check_reports(reports_list, False)
pretty_report(validated_reports_list)

count_of_valid_reports = []
count = 0
for report in validated_reports_list:
    if report["Validation"]:
        count = count + 1
print(count)
print()

reports_list = []
with open("reports.txt") as f:
    for report in f.readlines():
        reports_list.append(
            [int(number) for number in report.split(" ")]
        )

print(reports_list)

validated_reports_list = check_reports(reports_list, True)
count_of_valid_reports = []
count = 0
for report in validated_reports_list:
    if report["Validation"]:
        count = count + 1

pretty_report(validated_reports_list)
print(count)

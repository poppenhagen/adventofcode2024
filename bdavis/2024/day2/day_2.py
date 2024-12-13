def main():
    # file = open('./day2.txt')
    file = open('./day2_example.txt')
    safeReports = 0
    safeLeveledReports = 0
    while True:
        line = file.readline()
        if not line:
            break
        report = line.split(' ')

        report = [int(item) for item in report]

        increasing = True
        if report[0] > report[1]:
           increasing = False

        report_copy = report.copy()
        report_copy_2 = report.copy()
        print(report)
        if recurse(report, increasing):
            safeReports += 1

        report_copy.pop(0)
        report_copy_2.pop(0)
        print(report_copy)
        print(report_copy_2)
        if recurse_levels(report, increasing, False):
            safeLeveledReports += 1
        elif recurse(report_copy, increasing):
            safeLeveledReports += 1
        elif recurse(report_copy_2, not increasing):
            safeLeveledReports += 1
    print(safeReports)
    print(safeLeveledReports)


def recurse(report, increasing):
    if len(report) == 1:
        return True
    elif report[0] - report[1] == 0:
        return False
    elif increasing:
        if report[0] < report[1]:
            if report[1] - report[0] > 3:
                return False
            report.pop(0)
            return recurse(report, increasing)
        else:
            return False
    elif not increasing:
        if report[0] > report[1]:
            if report[0] - report[1] > 3:
                return False
            report.pop(0)
            return recurse(report, increasing)
        else:
            return False
    else:
        report.pop(0)
        return recurse(report, increasing)

def recurse_levels(report, increasing, leveled):
    if len(report) == 1:
        return True
    elif report[0] - report[1] == 0:
        if leveled:
            return False
        else:
            report.pop(1)
            return recurse_levels(report, increasing, True)
    elif increasing:
        if report[0] < report[1]:
            if report[1] - report[0] > 3:
                if leveled:
                    return False
                else:
                    report.pop(1)
                    return recurse_levels(report, increasing, True)
            report.pop(0)
            return recurse_levels(report, increasing, leveled)
        else:
            if leveled:
                return False
            else:
                report.pop(1)
                return recurse_levels(report, increasing, True)
    elif not increasing:
        if report[0] > report[1]:
            if report[0] - report[1] > 3:
                if leveled:
                    return False
                else:
                    report.pop(1)
                    return recurse_levels(report, increasing, True)
            report.pop(0)
            return recurse_levels(report, increasing, leveled)
        else:
            if leveled:
                return False
            else:
                report.pop(1)
                return recurse_levels(report, increasing, True)
    else:
        report.pop(0)
        return recurse_levels(report, increasing, leveled)



main()
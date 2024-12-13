
def main():
    file = open('./day5_example.txt')
    # file = open('./day5.txt')
    rules = []
    rule1 = []
    rule2 = []

    while True:
        line = file.readline()
        if not line or line.isspace():
            break
        num1, num2 = line.split('|')
        rules.append((int(num1), int(num2)))
        rule1.append(int(num1))
        rule2.append(int(num2))

    valid_lines = []
    invalid_lines = []
    while True:
        line = file.readline()
        if not line:
            break
        numbers = [int(item) for item in line.strip().split(",")]
        valid = True
        for i, num in enumerate(numbers):
            if num in rule2 and not follows_rules(rules, numbers, numbers[:i], num):
                valid = False

        if valid:
            valid_lines.append(numbers)
        else:
            for i, num in enumerate(numbers):
                fix_line(rules, numbers, numbers[:i], num)
            invalid_lines.append(numbers)

    total = 0
    for numbers in valid_lines:
        total += numbers[len(numbers)//2]
    print(total)
    # PART 2
    print(invalid_lines)
    total2 = 0
    for numbers in invalid_lines:
        total2 += numbers[len(numbers)//2]
    print(total2)



def follows_rules(rules, numbers, numbers_short, num):
    valid = True
    for rule in rules:
        if num == rule[1] and rule[0] in numbers and rule[0] not in numbers_short:
            valid = False
            break
    return valid

def fix_line(rules, numbers, numbers_short, num):
    for i, rule in enumerate(rules):
        if num == rule[1] and rule[0] in numbers and rule[0] not in numbers_short:
            new_i = numbers.index(rule[0])
            old_i = numbers.index(rule[1])
            numbers[old_i], numbers[new_i] = numbers[new_i], numbers[old_i]
main()
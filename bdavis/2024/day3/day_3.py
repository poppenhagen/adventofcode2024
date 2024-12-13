import re

def main():
    # with open('./day3_example.txt') as f:
    with open('./day3.txt') as f:
        data = f.read().rstrip()
        # print(data)
        expressions = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", data)

        total = 0
        for e in expressions:
            nums = e[4:-1]
            num1, num2 = nums.split(',')
            total += int(num1) * int(num2)
        print(total)

def main2():
    with open('./day3.txt') as f:
    # with open('./day3_example.txt') as f:
        data = f.read().rstrip()
        dont_iters = re.finditer("don't\(\)", data)
        do_iters = re.finditer("do\(\)", data)
        traverse = []
        for do in do_iters:
            traverse.append((do.start(), 'do'))
        for dont in dont_iters:
            traverse.append((dont.start(), 'dont'))
        expression_iters = re.finditer("mul\([0-9]{1,3},[0-9]{1,3}\)", data)
        expressions = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", data)
        for i, expression in enumerate(expression_iters):
            traverse.append((expression.start(), expressions[i]))
        traverse.sort()
        do = True
        total = 0
        for item in traverse:
            if item[1] == 'do':
                do = True
            elif item[1] == 'dont':
                do = False
            elif do:
                nums = item[1][4:-1]
                num1, num2 = nums.split(',')
                total += int(num1) * int(num2)

        print(total)
main()
main2()
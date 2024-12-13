
def main():
    # file = open('./day1.txt')
    file = open('./day1_example.txt')
    list1 = []
    list2 = []
    while True:
        line = file.readline()
        entries = line.split('   ')
        if not line:
            break
        list1.append(int(entries[0]))
        list2.append(int(entries[1]))

    list1.sort()
    list2.sort()

    total = 0
    for i, item in enumerate(list1):
        total += abs(list1[i] - list2[i])

    print(total)
main()

def main2():
    # file = open('./day1.txt')
    file = open('./day1_example.txt')
    list1 = []
    list2 = []
    while True:
        line = file.readline()
        entries = line.split('   ')
        if not line:
            break
        list1.append(int(entries[0]))
        list2.append(int(entries[1]))

    list1.sort()
    list2.sort()

    total = 0
    for item in list1:
        count = list2.count(item)
        total += item * count

    print(total)

main2()
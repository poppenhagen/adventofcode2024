
def main():
    file = open('./day4.txt')
    # file = open('./day4_example.txt')
    letters_array = []
    while True:
        line = file.readline()
        if not line:
            break
        letters_array.append(list(line.strip()))
    count = 0
    count_b = 0
    for r_idx, row in enumerate(letters_array):
        for l_idx, letter  in enumerate(row):
            if letter == 'X':
                if l_idx < len(letters_array[r_idx]) - 1 and letters_array[r_idx][l_idx+1] == 'M':
                    if l_idx < len(letters_array[r_idx]) - 2 and letters_array[r_idx][l_idx+2] == 'A':
                        if l_idx < len(letters_array[r_idx]) - 3 and letters_array[r_idx][l_idx+3] == 'S':
                            count += 1
                if l_idx >= 1 and letters_array[r_idx][l_idx - 1] == 'M':
                    if l_idx >= 2 and letters_array[r_idx][l_idx - 2] == 'A':
                        if l_idx >= 3 and letters_array[r_idx][l_idx - 3] == 'S':
                            count += 1
                if r_idx < len(letters_array) - 1 and letters_array[r_idx+1][l_idx] == 'M':
                    if r_idx < len(letters_array) - 2 and letters_array[r_idx+2][l_idx] == 'A':
                        if r_idx < len(letters_array) - 3 and letters_array[r_idx+3][l_idx] == 'S':
                            count += 1
                if r_idx >= 1 and letters_array[r_idx - 1][l_idx] == 'M':
                    if r_idx >= 2 and letters_array[r_idx - 2][l_idx] == 'A':
                        if r_idx >= 3 and letters_array[r_idx - 3][l_idx] == 'S':
                            count += 1
                if l_idx < len(letters_array[r_idx]) - 1 and r_idx < len(letters_array) - 1 and letters_array[r_idx + 1][l_idx + 1] == 'M':
                    if l_idx < len(letters_array[r_idx]) - 2 and r_idx < len(letters_array) - 2 and  letters_array[r_idx + 2][l_idx + 2] == 'A':
                        if l_idx < len(letters_array[r_idx]) - 3 and r_idx < len(letters_array) - 3 and  letters_array[r_idx + 3][l_idx + 3] == 'S':
                            count += 1
                if l_idx < len(letters_array[r_idx]) -1 and r_idx >= 1 and letters_array[r_idx - 1][l_idx + 1] == 'M':
                    if l_idx < len(letters_array[r_idx]) -2 and r_idx >= 2 and letters_array[r_idx - 2][l_idx + 2] == 'A':
                        if l_idx < len(letters_array[r_idx]) -3 and r_idx >= 3 and letters_array[r_idx - 3][l_idx + 3] == 'S':
                            count += 1
                if l_idx >= 1 and r_idx >= 1 and letters_array[r_idx - 1][l_idx - 1] == 'M':
                    if l_idx >= 2 and r_idx >= 2 and letters_array[r_idx - 2][l_idx - 2] == 'A':
                        if l_idx >= 3 and r_idx >= 3 and letters_array[r_idx - 3][l_idx - 3] == 'S':
                            count += 1
                if l_idx >= 1 and r_idx < len(letters_array) - 1 and letters_array[r_idx + 1][l_idx - 1] == 'M':
                    if l_idx >= 2 and r_idx < len(letters_array) - 2 and letters_array[r_idx + 2][l_idx - 2] == 'A':
                        if l_idx >= 3 and r_idx < len(letters_array) - 3 and letters_array[r_idx + 3][l_idx - 3] == 'S':
                            count += 1

    for r_idx, row in enumerate(letters_array):
        for l_idx, letter in enumerate(row):
            if letter == 'A':
                if r_idx == 0 or l_idx == 0:
                    continue
                if r_idx >= len(letters_array)-1 or l_idx >= len(letters_array[r_idx])-1:
                    continue
                if letters_array[r_idx+1][l_idx+1] == 'M' and letters_array[r_idx-1][l_idx-1] == 'S' and \
                        letters_array[r_idx-1][l_idx+1] == 'M' and letters_array[r_idx+1][l_idx-1] == 'S':
                    count_b += 1
                if letters_array[r_idx + 1][l_idx + 1] == 'M' and letters_array[r_idx - 1][l_idx - 1] == 'S' and \
                        letters_array[r_idx - 1][l_idx + 1] == 'S' and letters_array[r_idx + 1][l_idx - 1] == 'M':
                    count_b += 1
                if letters_array[r_idx + 1][l_idx + 1] == 'S' and letters_array[r_idx - 1][l_idx - 1] == 'M' and \
                        letters_array[r_idx - 1][l_idx + 1] == 'S' and letters_array[r_idx + 1][l_idx - 1] == 'M':
                    count_b += 1
                if letters_array[r_idx + 1][l_idx + 1] == 'S' and letters_array[r_idx - 1][l_idx - 1] == 'M' and \
                        letters_array[r_idx - 1][l_idx + 1] == 'M' and letters_array[r_idx + 1][l_idx - 1] == 'S':
                    count_b += 1
    print(count)
    print(count_b)


main()
def main():
    # file = open('./day6.txt')
    file = open('./day6_example.txt')
    letters_array = []
    row_location, column_location = 0, 0
    row_count = 0
    direction = 'up'
    while True:
        line = file.readline()
        if not line:
            break
        if '^' in line or '<' in line or '>' in line or 'v' in line:
            print('found')
            if '^' in line:
                direction = 'up'
            elif '>' in line:
                direction = 'right'
            elif '<' in line:
                direction = 'left'
            else:
                direction = 'down'
            row_location = row_count
            column_location = line.index('^')
        row_count += 1
        letters_array.append(list(line.strip()))
    print(row_location, column_location, direction)
    print(letters_array[row_location][column_location])

    count = 0
    while True:
        # if row_location < 0 or row_location > len(letters_array) or column_location < 0 or column_location > len(letters_array[row_location]):
        #     break
        count += 1
        letters_array[row_location][column_location] = 'X'
        if letters_array[row_location][column_location] == '#':
            if direction == 'up':
                direction == 'right'
            elif direction == 'down':
                direction == 'left'
            elif direction == 'right':
                direction == 'down'
            elif direction == 'left':
                direction == 'up'

        if direction == 'up':
            row_location -= 1
        elif direction == 'down':
            row_location += 1
        elif direction == 'left':
            column_location -= 1
        else:
            column_location += 1
        if row_location < 0 or row_location >= len(letters_array):
            break
        elif column_location < 0 or column_location >= len(letters_array[0]):
            break

    print(count)
main()
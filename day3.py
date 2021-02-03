data = []

with open('day3-data') as f:
    for line in f:
        data.append(line[0:-1])


def slope(right, down):
    x, y = 0, 0
    counter = 0
    width = len(data[0])

    while not y >= len(data) - 1:

        x += right
        y += down

        if x >= width:
            x -= width

        if data[y][x] == '#':
            counter += 1

    return counter


# part 1
print(slope(3, 1))

# part 2
print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
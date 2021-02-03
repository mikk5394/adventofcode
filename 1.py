#day1

#part 1
numbers = []

with open('1-data') as f:
    for line in f:
        numbers.append(int(line.strip("\n")))

for i in numbers:
    for k in numbers:
        if i+k == 2020:
            print(str(i) + ' ' + str(k))
            print(i*k)


#part 2

for i in numbers:
    for k in numbers:
        for j in numbers:
            if i+k+j == 2020:
                print(str(i) + ' ' + str(k) + ' ' + str(j))
                print(i*k*j)
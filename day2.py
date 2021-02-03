# part1
data = []

with open('day2-data') as f:
    for line in f:
        data.append(line.strip("\n"))

counter = 0

for i in data:
    amount = i.split(':')[0][0:-2]  # space between last number and letter, explains the -2
    letter = i.split(':')[0][-1]  # the letter to check on
    password = i.split(':')[1]  # the string we check for number of times the letter appears
    appearance = password.count(letter)  # doing the counting

    rangeOfNumbers = range(int(amount.split('-')[0]), int(amount.split('-')[1]))

    if rangeOfNumbers[0] <= appearance <= rangeOfNumbers[-1] + 1:  # +1 to have the last number in the range included
        counter += 1

# part2

counter = 0

for i in data:
    firstPos = int(i.split(':')[0].split('-')[0])
    secondPos = int(i.split(':')[0].split('-')[1][0:-2])
    letter = i.split(':')[0][-1]
    password = i.split(':')[1]

    if (password[firstPos] == letter and password[secondPos] != letter) or (password[firstPos] != letter and password[secondPos] == letter):
        counter += 1
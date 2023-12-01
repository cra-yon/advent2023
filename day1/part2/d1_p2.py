file = open('C:/advent2023/day1/part2/d1_p2_test', 'r')
lines = file.readlines()
file.close()

lookup = {
    'one' : 'o1e',
    'two' : 't2o',
    'three' : 't3e',
    'four' : 'f4r',
    'five' : 'f5e',
    'six' : 's6x',
    'seven' : 's7n',
    'eight' : 'e8t',
    'nine' : 'n9e'
}

for key, key_value in lookup.items():
    for index, line in enumerate(lines):
        print(index)
        lines[index] = line.replace(key, key_value)
        index = index + 1
          
print(lines)


precalibrationvalues = []

calibrationvalues = []

sum = 0

for line in lines:
    items = list(line)
    number = ''
    for i in items:
        if i.isnumeric():
            number = number + i
    precalibrationvalues.append(number)

for value in precalibrationvalues:
    number = ''
    number = number + value[0]
    number = number + value[-1]
    calibrationvalues.append(number)

for c in calibrationvalues:
    sum = sum + int(c)

print(precalibrationvalues)
print(calibrationvalues)
print(sum)


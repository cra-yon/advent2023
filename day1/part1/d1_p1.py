file = open('C:/advent2023/day1/d1_p1_test', 'r')
lines = file.readlines()
file.close()

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

#print(precalibrationvalues)
#print(calibrationvalues)
print(sum)


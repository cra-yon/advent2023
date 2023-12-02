file = open("C:/advent2023/day1/part2/d1_p2_test", "r")
lines = file.readlines()
file.close()

num_string = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0

def first_char(line):
    first_str = len(line)
    first_int = len(line)
    index_str = 0

    for ns in num_string:
        if line.indexOf(ns) < first_str: 
            first_str = ns

    for ni in num_int:
        if line.indexOf(ni) < first_int:
            first_int = ni

    if(first_str < first_int):
        return num_int[]
    else:
        return num_int[]



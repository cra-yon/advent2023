file = open("day4/input.txt", "r")
lines = file.readlines()
file.close()

win_nums, your_nums, sum = [], [], 0

for x, line in enumerate(lines):
    left_side, right_side = line.split('|')
    left_side = left_side.split(':')[1]
    win_nums.append(left_side.strip().split())
    your_nums.append(right_side.strip().split())

for x, win_num_list in enumerate(win_nums):
    match = 0
    for win_num in win_num_list:
        if win_num in your_nums[x]:
            match = match + 1
    if match > 0:
        points = 1
        while match > 1:
            points = points * 2
            match = match - 1
        sum = sum + points

print(sum)
file = open("wtf", "r")
D = file.read()
file.close()

S = ["*", '+', '$', "#", "/", "@", "%", '=', "&", "-"]

def part1():
  lines = D.splitlines()

  part_numbers = []

  for index, line in enumerate(lines):
    line_end = len(line)-1
    number_start = -1
    number_end = -1
    for line_index, char in enumerate(line):
      if char.isdigit() and number_start == -1:
        number_start = line_index
        number_end = line_index
      elif char.isdigit() and number_start != -1:
        number_end = line_index

      if number_start == -1 and number_end == -1:
        continue

      if char == "." or line_index == line_end or char in S:
        full_number = int(line[number_start:number_end+1])

        check_start = max(number_start - 1, 0)
        check_end = min(number_end + 1, line_end)
        
        is_adj = False

        if (check_start > 0 and line[check_start] in S):
          is_adj = True
        elif(check_end < line_end and line[check_end] in S):
          is_adj = True

        # check above and below
        for i in range(check_start, check_end + 1):
          above = index > 0 and lines[index -1][i] in S
          below = index < line_end and lines[index + 1][i] in S
          if above or below:
            is_adj = True
            break
          
        if is_adj:
          part_numbers.append(full_number)

        number_start = -1
        number_end = -1

  print("p1", sum(part_numbers), part_numbers)

if __name__ == '__main__':
  part1()
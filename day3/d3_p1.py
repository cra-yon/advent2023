file = open("d3_p1_test", "r")
data = file.read().splitlines()
file.close()

charlistlist, numbercoords, adjsymbolcoords = [], [], []

def init_matrix(lines):
    for line in lines:
        charlistlist.append(list(line))

def get_symbol_coords(matrix):
    coordlist = []
    for x, xitem in enumerate(matrix):
        for y, yitem in enumerate(matrix[x]):
            if not yitem.isnumeric() and not yitem == '.':
                coordlist.extend((x + xc, y + yc) for xc in range(-1, 2) for yc in range(-1, 2) if is_valid_coord(x + xc, y + yc))
    return coordlist

def get_numbers(matrix):
    numlist = []
    for x, xitem in enumerate(matrix):
        tempnum, coordlist = '', []
        for y, yitem in enumerate(matrix[x]):
            if yitem.isnumeric():
                tempnum = tempnum + yitem
                coordlist.append((x, y))
            elif tempnum:
                numlist.append((tempnum, coordlist))
                tempnum, coordlist = '', []
        if tempnum:
            numlist.append((tempnum, coordlist))
    return numlist
            
def is_adj_symbol_coord(x, y):
    return (x, y) in adjsymbolcoords

#this checks if a coordinate is in the bounds of the matrix
def is_valid_coord(x ,y):
    return x <= len(charlistlist) and y <= len(charlistlist[0])


init_matrix(data)
numbercoords = get_numbers(charlistlist)
adjsymbolcoords = get_symbol_coords(charlistlist)

numbersadjsymbols = []

for number in numbercoords:
    for coord in number[1]:
        if is_adj_symbol_coord(coord[0], coord[1]):
            numbersadjsymbols.append(int(number[0]))
            break

print(sum(numbersadjsymbols))
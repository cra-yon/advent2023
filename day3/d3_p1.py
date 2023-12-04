file = open("d3_p1_test", "r")
data = file.read().splitlines()
file.close()

charlistlist, numbercoords, adjsymbolcoords = [], [], []

def generatematrix(lines):
    for line in lines:
        charlistlist.append(list(line))

def getsymbolcoords(matrix):
    coordlist = []
    for x, xitem in enumerate(matrix):
        for y, yitem in enumerate(matrix[x]):
            if not yitem.isnumeric() and not yitem == '.':
                for xc in range(-1,2):
                    for yc in range(-1,2):
                        if(validcoord(x + xc, y + yc)):
                            coordlist.append((x + xc, y + yc))
    return coordlist

def generatenumbers(matrix):
    numlist = []
    for x, xitem in enumerate(matrix):
        tempnum, coordlist = '', []
        for y, yitem in enumerate(matrix[x]):
            if yitem.isnumeric():
                tempnum = tempnum + yitem
                coordlist.append((x, y))
            else:
                if tempnum != '':
                    numlist.append((tempnum, coordlist))
                    tempnum, coordlist = '', []
        if tempnum != '':
            numlist.append((tempnum, coordlist))
    return numlist
            
def isadjsymbolcoord(x, y):
    return (x, y) in adjsymbolcoords

#this checks if a coordinate is in the bounds of the matrix
def validcoord(x ,y):
    return x <= len(charlistlist) and y <= len(charlistlist[0])


generatematrix(data)
numbercoords = generatenumbers(charlistlist)
adjsymbolcoords = getsymbolcoords(charlistlist)

numbersadjsymbols = []

for number in numbercoords:
    for coord in number[1]:
        if isadjsymbolcoord(coord[0], coord[1]):
            numbersadjsymbols.append(int(number[0]))
            break

print(sum(numbersadjsymbols))
file = open("day3/d3_p1_test", "r")
data = file.read().splitlines()
file.close()

charlistlist = []
numbercoords = []
adjsymbolcoords = []

#putting all characters from file into a matrix
def generatematrix(lines):
    for line in lines:
        charlistlist.append(list(line))

#this returns a list of {x,y} pairs for any valid adjacent symbol coordinate
def getsymbolcoords(matrix):
    coordlist = []
    for x, xitem in enumerate(matrix):
        for y, yitem in enumerate(matrix[x]):
            #if char is not  number or a '.' 
            if not yitem.isnumeric() and not yitem == '.':
                # get all x-1 x x+1, y-1 y y+1 coordinate
                for xc in range(-1,2):
                    for yc in range(-1,2):
                        if(validcoord(x + xc, y + yc)):
                            # print('x : ' + str(x + xc))
                            # print('y : ' + str(y + yc))
                            coordlist.append((x + xc, y + yc))
    return coordlist

def generatenumbers(matrix):
    numlist = []
    for x, xitem in enumerate(matrix):
        tempnum = ''
        coordlist = []
        for y, yitem in enumerate(matrix[x]):
            if yitem.isnumeric():
                tempnum = tempnum + yitem
                #print(tempnum)
                coordlist.append((x, y))
            else:
                if tempnum != '':
                    numlist.append((tempnum, coordlist))
                    tempnum = ''
                    coordlist = []
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
            numbersadjsymbols.append(number[0])
            break

print(numbersadjsymbols)

sum = 0

for num in numbersadjsymbols:
    sum = sum + int(num)

print(sum)
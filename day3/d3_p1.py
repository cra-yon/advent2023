file = open("day3/d3_p1_test", "r")
data = file.read().splitlines()
file.close()

charlistlist = []
numbercoords = []
adjsymbolcoords = []

def generatematrix(lines):
    for line in lines:
        charlistlist.append(list(line))

def getnumcoords(matrix):
    coordlist = []
    for x, xitem in enumerate(matrix):
        for y, yitem in enumerate(matrix[x]):
            if yitem.isnumeric():
                coordlist.append({x, y})
    return coordlist


def getsymbolcoords(matrix):
    coordlist = []
    for x, xitem in enumerate(matrix):
        for y, yitem in enumerate(matrix[x]):
            if not yitem.isnumeric() and not yitem == '.':
                for xc in range(-1,2):
                    for yc in range(-1,2):
                        if(validcoord(x + xc, y + yc)):
                            coordlist.append({x + xc, y + yc})
    return coordlist

# def generatemumbers(list):

# def generatesum(list):

def validcoord(x ,y):
    return x <= len(charlistlist) and y <= len(charlistlist[0])


generatematrix(data)

print(charlistlist)

numbercoords = getnumcoords(charlistlist)
adjsymbolcoords = getsymbolcoords(charlistlist)

print(numbercoords)
print(adjsymbolcoords)

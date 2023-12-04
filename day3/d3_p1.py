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

#this returns a list of {x,y} pairs for any instance of a number
def getnumcoords(matrix):
    coordlist = []
    for x, xitem in enumerate(matrix):
        for y, yitem in enumerate(matrix[x]):
            if yitem.isnumeric():
                coordlist.append({x, y})
    return coordlist

#this returns a list of {x,y} pairs for any valid adjacent symbol coordinate
def getsymbolcoords(matrix):
    coordlist = []
    for x, xitem in enumerate(matrix):
        for y, yitem in enumerate(matrix[x]):
            #if char is not a number or a '.' 
            if not yitem.isnumeric() and not yitem == '.':
                # get all x-1 x x+1, y-1 y y+1 coordinate
                for xc in range(-1,2):
                    for yc in range(-1,2):
                        if(validcoord(x + xc, y + yc)):
                            coordlist.append({x + xc, y + yc})
    return coordlist

#this is not complete
def generatenumbers(matrix):
    for x, xitem in enumerate(matrix):
        tempnum = ''
        isvalid = False
        for y, yitem in enumerate(matrix):
            if yitem.isnumeric():
                tempnum = tempnum + yitem
            
def isadjsymbolcoord(x, y):
    return 


# def generatesum(list):

def validcoord(x ,y):
    return x <= len(charlistlist) and y <= len(charlistlist[0])


generatematrix(data)

#print(charlistlist)

numbercoords = getnumcoords(charlistlist)
adjsymbolcoords = getsymbolcoords(charlistlist)

#print(numbercoords)
print(adjsymbolcoords)

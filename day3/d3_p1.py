file = open("day3/d3_p1_test", "r")
data = file.read().splitlines()
file.close()

charlistlist = []
numbercoords = []
isadjsymbolcoords = []

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


# def getsymbolcoords(matrix):

# def generatemumbers(list):

# def generatesum(list):

# def validcoord(x ,y):

generatematrix(data)

print(charlistlist)

numbercoords = getnumcoords(charlistlist)

print(numbercoords)

file = open("day3/d3_p1_test", "r")
data = file.read().splitlines()
file.close()

charlistlist = []

def generatematrix(lines):
    for x, line in enumerate(lines):
        charlistlist.append(list(line))

# def getnumcoords(matrix):

# def getsymbolcoords(matrix):

# def generatemumbers(list):

# def generatesum(list):

# def validcoord(x ,y):

generatematrix(data)

print(charlistlist)

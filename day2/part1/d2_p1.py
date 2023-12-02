file = open("day2/part1/d2_p1_test", "r")
lines = file.read().splitlines()
file.close()
# print(lines)

#create game object - nevermind maybe a dictionary
#initialize r, g, b
#create a function to create a list of objects
#set object r, g, b to highest value associated with each value, rest don't matter

games = []
sum = 0

def create_game(line):
    #split by : and remove 'Game '
    game_id = line.split(':', 1)[0][5:]
    #print(game_id)
    turns = line.split(':', 1)[1].split(';')
    red = 0
    green = 0
    blue = 0
    for t in turns:
        #need to get the value for red, green, blue
        turn = [x.strip() for x in t.split(',')]
        #print(turn)
        for qty in turn:
            if 'red' in qty:
                red = max(red, int(qty[0:qty.index('red') - 1]))
            if 'green' in qty:
                green = max(green, int(qty[0:qty.index('green') - 1]))
            if 'blue' in qty:
                blue = max(blue, int(qty[0:qty.index('blue') - 1]))
    #print(game_id + ' red' + str(red) + ' green' + str(green) + ' blue' + str(blue))
    games.append({'game_id':game_id, 'red':red, 'green':green, 'blue':blue})
        
        


for line in lines:
    create_game(line)

for game in games:
    if(game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14):
        print(game['game_id'])
        sum = sum + int(game['game_id'])

print(sum)

print(*games, sep='\n')

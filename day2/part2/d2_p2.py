file = open("day2/part1/d2_p1_test", "r")
lines = file.read().splitlines()
file.close()

games = []
sum = 0

def create_game(line):
    game_id = line.split(':', 1)[0][5:]
    turns = line.split(':', 1)[1].split(';')
    red = 0
    green = 0
    blue = 0
    for t in turns:
        turn = [x.strip() for x in t.split(',')]
        for qty in turn:
            if 'red' in qty:
                red = max(red, int(qty[0:qty.index('red') - 1]))
            if 'green' in qty:
                green = max(green, int(qty[0:qty.index('green') - 1]))
            if 'blue' in qty:
                blue = max(blue, int(qty[0:qty.index('blue') - 1]))
    games.append({'game_id':game_id, 'red':red, 'green':green, 'blue':blue})
        
for line in lines:
    create_game(line)

for game in games:
    sum = sum + (game['red'] * game['green'] * game['blue'])

print(sum)


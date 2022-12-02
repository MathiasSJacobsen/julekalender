def RockPapirScissors(filename):
    with open(filename) as f:
        s = 0
        for line in f.readlines():
            line = line.strip().split()
            oponent = decode(line[0])
            player = decode(line[1])
            s += outcome(player, oponent)
        return s
    


def decode(a):
    if a == 'A':
        return 'rock'
    elif a == 'B':
        return 'paper'
    elif a == 'C':
        return 'scissors'
    elif a == 'Y':
        return 'paper'
    elif a == 'X':
        return 'rock'
    elif a == 'Z':
        return 'scissors'

def determined(player, oponent):
    d_points = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }
    
    
    if player == 'X':
        return lose(oponent, d_points)
    elif player == 'Y':
        return draw(oponent, d_points)
    else: return win(oponent, d_points)

def lose(oponent, points):
    d_lose = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    return points[d_lose[oponent]] + 0

def draw(oponent, points):
    return points[oponent] + 3

def win(oponent, points):
    d_win = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    return points[d_win[oponent]] + 6

def outcome(player, oponent):
    if player == 'rock' and oponent == 'rock':
        return 3 + 1
    elif player == 'rock' and oponent == 'paper':
        return 0 + 1
    elif player == 'rock' and oponent == 'scissors':
        return 6 + 1
    elif player == 'paper' and oponent == 'rock':
        return 6 + 2
    elif player == 'paper' and oponent == 'paper':
        return 3 + 2
    elif player == 'paper' and oponent == 'scissors':
        return 0 + 2
    elif player == 'scissors' and oponent == 'rock':
        return 0 + 3
    elif player == 'scissors' and oponent == 'paper':
        return 6 + 3
    elif player == 'scissors' and oponent == 'scissors':
        return 3 + 3

def RockPapirScissorsDetermined(filename):
    with open(filename) as f:
        s = 0
        for line in f.readlines():
            line = line.strip().split()
            oponent = decode(line[0])
            player = line[1]
            s += determined(player, oponent)
        return s

if __name__ == '__main__':
    print(RockPapirScissorsDetermined('2022/AoC/luke2.txt'))
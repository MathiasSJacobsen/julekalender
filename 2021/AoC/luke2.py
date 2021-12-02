def luke1Silver(filename):
    with open(filename) as file:
        lines = [tuple(e.strip().split()) for e in file.readlines()]
        horizontal = 0
        depth = 0
        for cmd, units in lines:
            units = int(units)
            if cmd == 'forward':
                horizontal += units
            elif cmd == 'down':
                depth += units
            elif cmd == 'up':
                depth -= units
        return depth * horizontal



# print(luke1Silver("luke2silver.txt"))

def luke2Gold(filepath):
    with open(filepath) as file:
        lines = [tuple(e.strip().split()) for e in file.readlines()]
        horizontal = 0
        depth = 0
        aim = 0
        for cmd, unit in lines:
            unit = int(unit)
            if cmd == 'forward':
                horizontal += unit
                depth += unit * aim
            elif cmd == 'down':
                aim += unit
            elif cmd == 'up':
                aim -= unit
        return horizontal * depth

print(luke2Gold('luke2Gold.txt'))
            
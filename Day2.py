from itertools import islice, tee

def main():
    with open('Input/day2.txt') as f:
        lines = [l.strip('\n') for l in f.readlines()]
    print('Part One')
    diving_submarine(lines)

    print('Part Two')
    diving_submarine_2(lines)


def diving_submarine(lines):
    x = depth = 0
    for line in lines:
        command, num = line.split(" ")
        num = int(num)
        if command == 'forward':
            x += num
        elif command == 'down':
            depth += num
        elif command == 'up':
            depth -= num
        else:
            print('bugei')
    print(x, ' ', depth, ' Result:', x*depth)


def diving_submarine_2(lines):
    x = aim = depth = 0
    for line in lines:
        command, num = line.split(" ")
        num = int(num)
        print(command, ' ', num)
        if command == 'forward':
            x += num
            if x != 0:
                depth += num*aim
        elif command == 'down':
            aim += num
        elif command == 'up':
            aim -= num
    print(x, ' ', depth, ' Result:', x*depth)


if __name__ == "__main__":
    main()

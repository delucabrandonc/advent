import os

def main():

    submarine = []
    horizontal, depth, aim = 0, 0, 0

    with open('submarine.txt', 'r') as f:
        lines = f.readlines()
        for x in lines:
            new = x.split(' ')
            submarine.append([ new[0], int(new[1].replace('\n', '')) ])
        f.close()
    
    # Part 1
    # Submarine Directions
    for x in submarine:
        if x[0] == 'forward':
            horizontal += x[1]
        elif x[0] == 'up':
            depth -= x[1]
        else:
            depth += x[1]
    print('\nPart 1')
    print('Final Horizontal : ' + str(horizontal) + '\nFinal Depth : ' + str(depth))
    product = horizontal * depth
    print('Final Multiplication : ' + str(product) + '\n')

    # Part 2
    # Aim
    horizontal, depth, aim = 0, 0, 0

    for x in submarine:
        if x[0] == 'forward':
            horizontal += x[1]
            depth += aim * x[1]
        elif x[0] == 'up':
            aim -= x[1]
        else:
            aim += x[1]
    print('Part 2')
    print('Final Horizontal : ' + str(horizontal) + '\nFinal Depth : ' + str(depth))
    product = horizontal * depth
    print('Final Multiplication : ' + str(product) + '\n')



if __name__ == "__main__":
    main()
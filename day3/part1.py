def read_input(input_data):
    return [line.strip() for line in input_data.splitlines()]



def main(input_data):
    lines = read_input(input_data)
    trees = 0
    width = len(lines[0])
    x = 0
    for y in range(1, len(lines)):
        x+=3
        if lines[y][x%width] == '#':
            trees += 1
    return trees


        


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        print(main(file.read()))

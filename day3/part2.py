def read_input(input_data):
    return [line.strip() for line in input_data.splitlines()]



def main(input_data):
    lines = read_input(input_data)
    slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
    width = len(lines[0])
    res = 1
    for slope in slopes:
        x = 0
        trees = 0
        for y in range(0, len(lines), slope[1]):
            if lines[y][x%width] == '#':
                trees += 1
            x+=slope[0]
        res*=trees
    return res


        


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        print(main(file.read()))

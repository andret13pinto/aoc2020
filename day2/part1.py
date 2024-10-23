def read_input(input_data):
    return [int(line.strip()) for line in input_data.splitlines()]



def main(input_data):
    lines = read_input(input_data)
    for i in range(2020):
        if i in lines and 2020 - i in lines:
            return i * (2020 - i)



if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        print(main(file.read()))

def read_input(input_data):
    return [line.strip() for line in input_data.splitlines()]



def main(input_data):
    lines = read_input(input_data)
    res = 0
    for line in lines:
        nr_range, char, pwd = line.split()
        char = char[0]
        low_range, high_range  = int(nr_range.split('-')[0]), int(nr_range.split('-')[1])
        if pwd[low_range-1] == char and pwd[high_range-1] != char or \
           pwd[low_range-1] != char and pwd[high_range-1] == char:
               res+=1
    return res



if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        print(main(file.read()))

def read_input(input_data):
    return [content.strip() for content in input_data.split('\n\n')]



def main(input_data):
    passports = read_input(input_data)
    valid = 0
    fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for passport in passports:
        present_fields = [entry.split(':')[0] for entry in passport.split()]
        if set(fields).issubset(present_fields):
            valid+=1
    return valid



if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        print(main(file.read()))

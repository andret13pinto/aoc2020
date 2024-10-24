
FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def read_input(input_data):
    return [content.strip() for content in input_data.split('\n\n')]


def _is_hexadecimal(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False



def _is_valid_passport(passport):
    
    present_fields = [entry.split(':')[0] for entry in passport.split()]
    
    if not set(FIELDS).issubset(present_fields):
        return False

    for key, value in (entry.split(':') for entry in passport.split()) :
        match key:
            case 'byr':
                if not(len(value) == 4 and 2002 >= int(value) >= 1920):
                    return False
            case 'iyr':
                 if not(len(value) == 4 and 2020 >= int(value) >= 2010):
                     return False
            case 'eyr':
                 if not(len(value) == 4 and 2030 >= int(value) >= 2020):
                     return False
            case 'hgt':
                height, scale = value[:-2], value[-2:]
                match scale:
                    case 'in':
                        if not 76 >= int(height) >= 59:
                            return False
                    case 'cm':
                        if not 193 >= int(height) >= 150:
                            return False
                    case _:
                        return False

            case 'hcl':
                if not(value[0] == '#' and len(value) == 7 and \
                        _is_hexadecimal(value[1:])):
                    return False
            case 'ecl':
                if not value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    return False
            case 'pid':
                if not (value.isdigit() and len(value) == 9):
                        return False

    return True



def main(input_data):
    passports = read_input(input_data)
    valid = 0
    for passport in passports:
        if _is_valid_passport(passport):
            valid+=1
    return valid



if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        print(main(file.read()))

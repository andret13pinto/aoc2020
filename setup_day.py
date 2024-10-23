import requests
import argparse
import os
import shutil

from dotenv import load_dotenv

BASE_URL = 'https://adventofcode.com/2020/day/'


def _get_cookies():
    load_dotenv()
    return {'session': os.getenv('SESSION_COOKIE')}


def main():


    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="Day of the month")
    args = parser.parse_args()

    input_ = requests.get(f'{BASE_URL}{args.day}/input', cookies=_get_cookies())
    
    day = args.day
    day_path = f'day{day}'

    if input_.status_code == 200:
        shutil.copytree('day1', day_path)
        with open(f'{day_path}/input.txt', 'w') as file:
            file.write(input_.text)
        print("Saved input.txt")
        return 

    print(input_.status_code)
    print(input_.raise_for_status())





if __name__ == '__main__':
    main()


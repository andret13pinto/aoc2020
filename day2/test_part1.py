import pytest

import part1


INPUT = '''\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
'''

result = 2

def test():
    assert part1.main(INPUT) == result

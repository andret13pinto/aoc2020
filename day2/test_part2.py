import pytest

import part2


INPUT = '''\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
'''

result = 1

def test():
    assert part2.main(INPUT) == result

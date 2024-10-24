import pytest

import part1


INPUT = '''\
1721
979
366
299
675
1456
'''

result = 514579

def test():
    assert part1.main(INPUT) == result

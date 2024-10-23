import pytest

import part2


INPUT = '''\
1721
979
366
299
675
1456
'''

result = 241861950

def test():
    assert part2.main(INPUT) == result

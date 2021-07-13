import pytest
from no_fac import no_fac


@pytest.mark.timeout(1.0)
def test_no_fac__1():
    assert no_fac(3) == [0]
    assert no_fac(4) == [0, 3]
    assert no_fac(5) == [0, 3, 4]
    assert no_fac(10) == [0, 3, 4, 5, 7, 8, 9]
    assert no_fac(25) == [0, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21, 23]

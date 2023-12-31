import pytest
from dentist import take_maximum


@pytest.mark.timeout(1.0)
def test_dentist_1():
    # Example
    assert take_maximum(40, 80, 300) == (415.0, 75.0)


@pytest.mark.timeout(1.0)
def test_dentist_2():
    # Government is being a-holes
    assert take_maximum(0, 50, 420) == (420.0, 210.0)
    assert take_maximum(0, 20, 100) == (100.0, 80.0)
    assert take_maximum(0, 5, 6000) == (6000.0, 5700.0)


@pytest.mark.timeout(1.0)
def test_dentist_3():
    # No insurance
    assert take_maximum(20, 0, 0) == (40.0, 20.0)
    assert take_maximum(45, 0, 0) == (90.0, 45.0)
    assert take_maximum(13, 0, 0) == (26.0, 13.0)


@pytest.mark.timeout(1.0)
def test_dentist_4():
    # Combination of zeros
    assert take_maximum(0, 0, 0) == (0.0, 0.0)
    assert take_maximum(20, 0, 0) == (40.0, 20.0)
    assert take_maximum(0, 15, 400) == (400.0, 340.0)


@pytest.mark.timeout(1.0)
def test_dentist_5():
    # Actual test cases
    assert take_maximum(60, 70, 50) == (131.43, 21.43)
    assert take_maximum(30, 60, 200) == (363.33, 133.33)
    assert take_maximum(600, 20, 400) == (1200.0, 480.0)
    assert take_maximum(600, 20, 10) == (1200.0, 590.0)


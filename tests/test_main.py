from programik import calculate_bmi, process_row
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def test_calculate_bmi():
    bmi = calculate_bmi(150, 65)
    assert round(bmi, 2) == 24.96


def test_process_row():
    row = ["1", "65", "150"]
    index, height, weight, bmi = process_row(row)

    assert index == "1"
    assert height == 65.0
    assert weight == 150.0
    assert round(bmi, 2) == 24.96


def test_invalid_height():
    row = ["1", "abc", "150"]

    try:
        process_row(row)
        assert False 
    except ValueError:
        assert True
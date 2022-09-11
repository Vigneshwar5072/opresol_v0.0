import pytest
from taskTwoThreeMainFile import *


def test_happyPath():

    assert clubs_with_largest_number_of_players(6) is not None, "Returned value is not None but it should have 6 valid entries"
    assert len(clubs_with_largest_number_of_players(15)) == 15, "Returned value is not None but it should have 15 valid entries"
    assert len(clubs_with_largest_number_of_players(8)) == 2, "Returned value is 8 not 2 hence wrong comparsion making sense"


def test_sadPath():
    assert clubs_with_largest_number_of_players(-1) is None, "Returned value is should have None entries because given argument is -1"
    assert clubs_with_largest_number_of_players(999) is  None, "Returned value is should have None entries because given argument is 999"
    assert clubs_with_largest_number_of_players("kkl") is None, "Returned value is should have None entries because given argument is string"


if __name__ == "__main__":
    test_happyPath()
    test_sadPath()
    print("Everything passed")

import pytest
from taskTwoFiveMainFile import *


def test_happyPath():

    assert most_popular_nationality(6) is not None, "Returned value is not None but it should have 6 valid entries"
    popularNation = most_popular_nationality(9)
    assert len(popularNation) == 9, "the list consists of 9 elements as expected" 
    popularNation = most_popular_nationality(10)
    assert len(popularNation) == 10, "the list consists of 10 elements as expected"
    popularNation = most_popular_nationality(0)
    assert len(popularNation) == 0, "the list consists of 0 elements as expected"

def test_sadPath():
    assert most_popular_nationality(-1) is None, "Returned value is should have None entries because given argument is -1"
    assert most_popular_nationality(999) is  None, "Returned value is should have None entries because given argument is 999"
    assert most_popular_nationality("myName") is None, "Returned value is should have None because given argument is string"

if __name__ == "__main__":
    test_happyPath()
    test_sadPath()
    print("Everything passed")

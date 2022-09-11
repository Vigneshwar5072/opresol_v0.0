import pytest
from taskTwoFourMainFile import *


def test_happyPath():

    assert most_popular_nation_and_team_position(6) is not None, "Returned value is not None but it should have 6 valid entries"
    [nation, team] = most_popular_nation_and_team_position(9)
    assert len(nation) == 9, "the list consists of 9 elements as expected" 
    [nation, team] = most_popular_nation_and_team_position(10)
    assert len(team) == 10, "the list consists of 10 elements as expected"
    [nation, team] = most_popular_nation_and_team_position(0)
    assert len(nation) == 0, "the list consists of 0 elements as expected"

def test_sadPath():
    assert most_popular_nation_and_team_position(-1) is None, "Returned value is should have None entries because given argument is -1"
    assert most_popular_nation_and_team_position(999) is  None, "Returned value is should have None entries because given argument is 999"
    assert most_popular_nation_and_team_position("kkl") is None, "Returned value is should have None because given argument is string"

if __name__ == "__main__":
    test_happyPath()
    test_sadPath()
    print("Everything passed")

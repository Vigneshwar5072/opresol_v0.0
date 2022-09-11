import pytest
from taskTwoTwoMain import *


def test_happyPath():
    assert large_number_of_players_with_contracts_ends_in_twentyone(5) is not None, "Returned value is not None but it should have some valid entries"
    assert len(large_number_of_players_with_contracts_ends_in_twentyone(2)) == 2, "Returned value is not None but it should have some valid entries"
    assert len(large_number_of_players_with_contracts_ends_in_twentyone(8)) == 2, "Returned value is 8 not 2 hence wrong comparsion making sense"


def test_sadPath():
    assert large_number_of_players_with_contracts_ends_in_twentyone(-1) is None, "Returned value is not None but it should have some valid entries"
    assert large_number_of_players_with_contracts_ends_in_twentyone(999) is  None, "Returned value is not None but it should have some valid entries"
    assert large_number_of_players_with_contracts_ends_in_twentyone("kkl") is None, "Returned value is not None but it should have some valid entries"





if __name__ == "__main__":
    test_happyPath()
    test_sadPath()
    print("Everything passed")

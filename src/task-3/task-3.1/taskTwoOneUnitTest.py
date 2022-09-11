import pytest
from taskTwoOne import *


def test_happyPath():
    #min_capacity = input("What is the number of top improved performers needed?(x)")
    [skillSet, param_dict] = skillset(5)
    print("exists" if 'skill_fk_accuracy' in skillSet else "not existing")
    top_performed_improvement  = top_improvements(2)
    [skillSet, param_dict] = skillset(3)
    assert skillSet is not None, "this list should contain elements"



def test_sadPath():
    #min_capacity = input("What is the number of top improved performers needed?(x)")
    [skillSet, param_dict] = skillset(5)
    print("existing "if 'skill_fk_accuracy2' in skillSet else "not existing")
    [skillSet, param_dict] = skillset(-2)
    assert skillSet is None, "this list should contain None elements, because passed value is -ve"
    [skillSet, param_dict] = skillset(999)
    assert skillSet is None, "this list should contain None elements, because passed value is > 100"
    [skillSet, param_dict] = skillset("kkl")
    assert skillSet is None, "this list should contain None elements, because passed value is string"




if __name__ == "__main__":
    test_happyPath()
    test_sadPath()
    print("Everything passed")









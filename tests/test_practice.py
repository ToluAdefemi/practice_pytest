from lib.greet import greet 


def tests_greet():
    assert greet("Tolu")  == f"Hello, Tolu!"
    assert greet("") == f"Please enter a name"
    assert greet("Kevin Adefemi") == f"Hello, Kevin Adefemi!"
from lib.functions.greet import *
from lib.functions.add_five import *
from lib.classes.counter import *
from lib.classes.string_builder import *
from lib.classes.present import *

def tests_greet():
    assert greet("Tolu")  == f"Hello, Tolu!"
    assert greet("") == f"Please enter a name"
    assert greet("Kevin Adefemi") == f"Hello, Kevin Adefemi!"

def tests_add_five():
    assert add_five(5) == 10 
    assert add_five(23) == 28

def tests_report_length():
    assert report_length("Let's count the length of this") == "This string is 30 characters long."
    assert report_length("Check string length") == "This string is 19 characters long."

#Test for classes 

def tests_counter():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5
    assert counter.report() == "Counted to 5 so far."


def tests_string_builder_add():
    string = StringBuilder()
    string.add("Hello World.")
    assert string.str == "Hello World."

def tests_string_builder_size():
    string = StringBuilder()
    string.add("Hello World.")
    assert string.size() == 12

def test_string_builder_output():
    string = StringBuilder()
    string.add("Hello World.")
    string.output() == "Hello World."

import pytest

def test_present_wrap():
    present = Present()
    present.wrap('Game Console')
    assert present.contents == 'Game Console' #Testing wrap function

    with pytest.raises(Exception) as e:
        present.wrap('Another Item') #Testing error handling
    assert str(e.value) == "A contents has already been wrapped"


def test_present_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped"

    present.wrap('Nintendo DSI')
    assert present.unwrap() == "Nintendo DSI"


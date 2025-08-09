# Chapter 2 Exercise 1: Simple Message
# 1: Create a file named "simple_message.py"
# 2: Create a variable named simple_message and assign it "Hello Python World!"
# 3: Print simple_message

import pytest
from os import path

def test_simple_message_file_exists():
    test_path = path.abspath(__file__)
    exercise_directory = test_path.removesuffix("test_simple_message.py")
    simple_message_test_path = exercise_directory + "simple_message.py"
    assert path.exists(simple_message_test_path)
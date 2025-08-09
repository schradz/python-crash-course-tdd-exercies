# Chapter 1 Exercise: Hello World
# Directions: Create a file named hello_world.py that prints out "Hello World!"

import pytest
from os import path
import subprocess
from sys import executable

def test_hello_world_file_exists():
    assert path.exists("hello_world.py")


def test_hello_world_prints_correctly():
    result = subprocess.run(
        [executable, "hello_world.py"],
        capture_output=True,
        text=True   #capture output as string, not as byte sequence
    )

    assert result.stdout == "Hello World!\n"
    assert result.returncode == 0
    
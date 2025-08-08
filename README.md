# python-crash-course-tdd-exercies

# Description
This project is intended to follow along with "Python Crash Course 2nd Edition" 
while making use of Pytest to practice test driven development. The book is
broken down into two parts which focus on the basics of the Python programming
language and some project based applications. The Python Basics folder will
contain the solutions to chapter exercises that are seen while following the 
book, but will also contain a test file that will be used to validate the 
solution.

## Part 1: Python Basics
This part of the book is about teaching basics concepts needed for writing 
programs. There are 11 chapters that make up part one of the book:
    1. Getting Started
    2. Variables and Simple Data Types
    3. Introducing Lists
    4. Working with Lists
    5. If Statements
    6. Dictionaries
    7. User Input and While Loops
    8. Functions
    9. Classes
    10. Files and Exceptions
    11. Testing your Code

# Testing
The test files that will validate the chapter exercises will be written using
Pytest, a popular testing framwork.

# Getting Started
Create a virtual environment for this project. Creating a virtual environment
allows for dependencies across different python projects on your system to be 
contained, preventing conflicts.

Python has a package that allows for creating a virtual environment called venv.

## Linux
Run the following command to create the virtual environment:
    python3 -m venv {Your Virtual Directory}
    Note: Replace {Your Virtual Directory} with your desired directory name

To activate the virtual environment, execute the following command:
    ./{Your Virtual Directory}/bin/activate
    Note: To deactivate the virtual environment at any time, type "deactivate"

Run the following command to install the required packages for this project:

    pip install -r requirements.txt

Your project should now be setup


📘 README.md — 0. Integers addition
✨ Description

This project focuses on Test-Driven Development (TDD) in Python.
The goal of this task is to write a function that adds two integers while ensuring proper validation, documentation, and doctest coverage.

The function must handle integers and floats, raise appropriate exceptions, and follow Holberton’s TDD workflow: write tests first, then implement the function.

📌 Function Prototype
def add_integer(a, b=98):

✔ Requirements:

a and b must be integers or floats.

If either is not an integer or float → raise:

TypeError("a must be an integer")

TypeError("b must be an integer")

Floats must be cast to integers before addition.

Must return an int.

No modules can be imported.

📁 Files
File	Description
0-add_integer.py	Contains the add_integer function with full documentation
tests/0-add_integer.txt	Contains doctest test cases to validate behavior
🧪 Running Tests

Execute all doctests using:

python3 -m doctest ./tests/0-add_integer.txt -v


Expected output:

9 passed and 0 failed.
Test passed.

📝 Example Usage
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98

⚠️ Error Handling
>>> add_integer(4, "School")
TypeError: b must be an integer

>>> add_integer(None)
TypeError: a must be an integer

👨‍💻 Author

Fahad Abdulaziz Al-Ghamdi
Holberton School — Higher Level Programming

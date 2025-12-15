# Python - Inheritance

## Description

This project focuses on **Object-Oriented Programming (OOP)** in Python, specifically on **Inheritance**. It explains how classes can inherit attributes and methods from other classes, how to override them, and how to use built-in functions related to inheritance.

The goal is to understand the relationship between **base classes (superclasses)** and **derived classes (subclasses)** and apply inheritance correctly following Python best practices.

---

## Learning Objectives

By completing this project, you will be able to explain:

* What a **superclass / baseclass / parentclass** is
* What a **subclass / childclass** is
* How to list all attributes and methods of a class or instance
* When an instance can have new attributes
* How to inherit a class from another
* How to define a class with **multiple base classes**
* What is the default class every class inherits from
* How to override a method or attribute inherited from a base class
* Which attributes and methods are inherited by subclasses
* The purpose of inheritance
* How and when to use:

  * `isinstance()`
  * `issubclass()`
  * `type()`
  * `super()`

---

## Requirements

### Python Scripts

* Allowed editors: `vi`, `vim`, `emacs`
* Python version: **Python 3.8.5** (Ubuntu 20.04 LTS)
* All files must end with a new line
* The first line of every file must be:

  ```bash
  #!/usr/bin/python3
  ```
* Code must follow **pycodestyle (version 2.7.*)**
* All files must be executable
* File length will be checked using `wc`

### Python Test Cases

* Allowed editors: `vi`, `vim`, `emacs`
* All tests must be inside a `tests/` directory
* Test files must have a `.txt` extension
* Tests are executed using:

  ```bash
  python3 -m doctest ./tests/*
  ```

---

## Documentation

* All modules must have documentation:

  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  ```
* All classes must have documentation:

  ```bash
  python3 -c 'print(__import__("my_module").MyClass.__doc__)'
  ```
* All functions must have documentation:

  ```bash
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
  ```

Documentation must be a **complete sentence** describing the purpose of the module, class, or function.

⚠️ **Important:** Do NOT use the words `import` or `from` inside comments or documentation.

---

## Project Structure

```text
.
├── README.md
├── *.py
└── tests/
    └── *.txt
```

---

## Usage Example

```python
class Base:
    """Base class"""
    pass

class User(Base):
    """User class inheriting from Base"""
    pass
```

---

## Author

**Fahad bin Abdulaziz Al-Ghamdi**

Computer Science Graduate | Python Developer

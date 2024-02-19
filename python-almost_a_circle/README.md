# Almost a Circle - Python Project

## Introduction
This Python project, "Almost a Circle," aims to implement functionalities related to shapes, particularly rectangles and squares. The project focuses on object-oriented programming principles and emphasizes proper documentation, testing, and adherence to coding standards.

## Requirements
- **Python Scripts**
  - All Python scripts should be compatible with Python 3.8.5.
  - Use the following shebang at the beginning of each script: `#!/usr/bin/python3`.
  - Ensure that all files are executable.
  - Adhere to the PEP 8 style guide using the `pycodestyle` tool.
- **README.md**
  - A README.md file at the root of the project folder is mandatory.
- **Documentation**
  - Document all modules, classes, and functions using docstrings.
  - Provide meaningful explanations in the documentation to describe the purpose of each module, class, and method.
- **Unit Tests**
  - Use the `unittest` module for writing unit tests.
  - Organize test files and folders according to the project's structure.
  - Prefix test files and folders with `test_`.
  - Ensure all tests can be executed using `python3 -m unittest discover tests`.

## Project Structure
The project structure should follow these guidelines:
```
almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
└── tests/
    ├── test_models/
    │   ├── __init__.py
    │   ├── test_base.py
    │   ├── test_rectangle.py
    │   └── test_square.py
    └── __init__.py
```

## Usage
To execute the unit tests, use the following command:
```
python3 -m unittest discover tests
```
You can also run tests file by file:
```
python3 -m unittest tests/test_models/test_base.py
```

## Collaboration
Collaborate with your team members on writing test cases to ensure comprehensive test coverage and catch any potential edge cases. Communication and teamwork are essential for the success of this project.

## Author
This project is authored by [Saif Chaari].

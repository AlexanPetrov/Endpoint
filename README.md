# Directory Management Project

This project simulates a directory structure with commands to create, move, delete, and list directories. The solution is implemented in Python with logging to track actions & errors. Unit testing is utilized with pytest to validate each command's functionality.

No helper libraries are used except for pytest for testing convinience purposes.
Solution does not create folders on host machine. Input is taken and output is produced. 

# Project structure (excluding .gitignore and all files marked in it)

└── Endpoint
    ├── README.md
    ├── logs
    │   ├── commands.log
    │   └── errors.log
    ├── requirements.txt
    ├── sample_output.txt
    ├── src
    │   ├── directories.py
    │   ├── directory_node.py
    │   ├── directory_tree.py
    │   └── logging_config.py
    └── tests
        ├── conftest.py
        ├── test_create.py
        ├── test_delete.py
        ├── test_list.py
        └── test_move.py

# Setup Instructions

git clone <repository-url>
cd Endpoint

# Environment Setup

python3 -m venv .venv

source .venv/bin/activate

<!-- To exit Virtual environment: -->
deactivate 

# Install dependencies

pip3 install -r requirements.txt

<!-- To add more requirements -->
pip3 freeze > requirements.txt

# Run the Script

cd src
python3 directories.py

# Test Commands

CREATE <path>
MOVE <source-path> <destination-path>
DELETE <path>
LIST
exit

# Run the Tests

cd Endpoint 
pytest tests/ -v

# Python Version and Package Manager

This project uses Python 3 and pip3 for package management. 
If your system defaults to python & pip for Python 3 and pip3, please use python & pip.

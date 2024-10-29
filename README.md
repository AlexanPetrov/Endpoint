# Directory Management Project

This project simulates a directory structure with commands to **create**, **move**, **delete**, and **list** directories. The solution is implemented in **Python** with logging to track actions & errors. Unit testing is utilized with **pytest** to validate each command's functionality.

No helper libraries are used except for **pytest** for testing convenience purposes.  
Solution does not create folders on the host machine. Input is taken and output is produced.

## Setup Instructions

mkdir `<project-directory>`  
cd `<project-directory>`  
git clone https://github.com/AlexanPetrov/Endpoint.git  
cd Endpoint  

## Environment Setup

python3 -m venv .venv  

source .venv/bin/activate  

> To exit the virtual environment:  
deactivate  

## Install dependencies  

pip3 install -r requirements.txt  

> To update `requirements.txt` with any additional packages:  
pip3 freeze > requirements.txt  

## Run the Script  

cd src  
python3 directories.py  

## Test Commands  

- `CREATE <path>`  
- `MOVE <source-path> <destination-path>`  
- `DELETE <path>`  
- `LIST`  
- `exit`  

## Run the Tests  

cd Endpoint  
pytest tests/ -v  

## Python Version and Package Manager  

This project uses Python 3 and pip3 for package management.  
If your system defaults to `python` & `pip` for Python 3 and pip3, please use `python` & `pip` instead.  

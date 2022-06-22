# Secure By Design

A repository to show-off different techniques, to increase the security of the code.

## Getting started

Step one is to install Python 3. If you have not done this already you 
can follow the guide: 
  - [](https://realpython.com/installing-python/)

Then install the current environment and install the requirements:

```bash
python -m venv .env
python -m pip install -r requirements.txt
```

## Process documentation

### Initial Python Setup

Create a Python environment

```bash
python3 -m venv .env                      # Create Python Environment
```

The first time we need to install them directly;

```bash
python -m pip install django
```

Freeze the requirements, so that other people can use it.

```bash
python -m pip freeze > requirements.txt  # Freeze requirements
```

Run django's startproject in the current folder

```bash
python -m django startproject secure_by_design .
```


### Run Git

Add a gitignore from https://www.toptal.com/developers/gitignore/api/python,macos,django

```bash
git init
git add . 
```





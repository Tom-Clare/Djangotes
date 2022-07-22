# Djangotes

## Localhost instructions
Get a "Hello, world!" Python script running on your computer.

Clone this repository.

Navigate to the root directory of this project, the same folder as the .git and .gitignore files.

Create a virtual environment: `python3 -m venv [environment-name]` (I called mine djangotes-venv)

Activate your virtual environment: `. [environment-name]/bin/activate`

Ensure your pip program will run from the virtual environment: `which pip` (Expected output: `[directory to proj root]/[environment-name]/bin/pip)

Install Django with your virtual environment's pip: `pip install django`

Navigate `[proj root]/Djangotes`. This directory should contain `Djangotes`, `notes`, `manage.py`, and some DB file.

Begin the server: `python3 manage.py runserver`

Go to `localhost:8000/notes`.

Enjoy!

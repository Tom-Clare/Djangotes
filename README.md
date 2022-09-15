# How to get Djangotes working

This page tells you all you need to know to get a local version of Djangotes running. This will enable you to see how your credentials are used to connect to Authwave's servers, as well as providing an example on how to use Authwave's authentication tools in your project. Below is an abridged step-by-step if you just need a refresher. An extended guide is provided further down which includes some notes and more in-depth infomation.

## Abridged Guide

1. Clone the Djangotes repository.
2. Create and activate your virtual environment
3. Install the `django` and `authwave` libraries.
4. Insert your API key into `notes/authConfig.py`.
5. Run `python3 manage.py runserver 8080`.

## Extended Guide

### Cloning the repository
First off, you'll need to clone the repo so that you have a local copy of the code to run. To do this, open the repository in your browser of choise, click "clone or download", and copy the path to the `.git` file. Then, open up your command prompt, navigate to where you'd like to download the repository to, and type `git clone [url]`. After running that command, you should have a local copy of the Djangotes code.

### Your virtual environment
From here, you can create your virtual environment. To do that, run `python3 -m venv [new venv name]`. The gitignore file already includes entries for `venv` and `django-venv`, but feel free to use what makes sense for you.

Activate your virtual environment using `. [your venv name]/bin/activate`. Now, you can install components that pertain only to this project. If you want to make sure that worked properly, you can run `which pip`. This should return a path to a pip executable located in your new virtual environment. Check the path is correct, otherwise the libraries we are about to install may not configure properly.

### Dependencies
This project depends on the Django and Authwave libraries. To install them, run `pip install django` and `pip install authwave`. You *can* install from the included `requirements.txt` file using `pip install requirements.txt`, but we recommend installing the two libraaries independantly, as this will give you a better grasp on how you might set up your own project.

### Credentials
Open `notes/authConfig.py` and replace the placeholder API key with your API key (which can be retrieved from your Authwave portal). Authentication with the Authwave servers is partly done through the URL of your site. If you are running this project locally, you should use the `localhost:8080` site credentials issued by Authwave. Make sure to use the correct creentials when implementing Authwave into your project.

### Starting the server
That's all the setup completed! To see Djangotes in action, navigate to Django's root directory (the directory contianing `manage.py`) and run `python3 manage.py runserver 8080`.
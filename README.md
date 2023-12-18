# Installation Instructions

Installing Django
pip is the package manager for Python. Django is distributed as a pip package, making it very easy to install in our new virtual environment:

# Windows Setup
PS C:\Users\USERNAME\cs631_project> pip install django
PS C:\Users\USERNAME\cs631_project> pip install djangorestframework
PS C:\Users\USERNAME\cs631_project> py .\manage.py makemigrations
PS C:\Users\USERNAME\cs631_project> py .\manage.py migrations
PS C:\Users\USERNAME\cs631_project> py .\manage.py runserver

If you get this error on Windows follow the instructions at this link below:
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
https://stackoverflow.com/questions/65348890/python-was-not-found-run-without-arguments-to-install-from-the-microsoft-store

# Unix-Based setup
~/cs631_project> pip install django
~/cs631_project> pip install djangorestframework
~/cs631_project> python3 manage.py makemigrations
~/cs631_project> python3 manage.py migrations
~/cs631_project> python3 manage.py runserver


Due to size limitations, I am unable to upload the files for creating the json that stores first and last names. As such the link to these files is provided here, also available on GitHub https://github.com/philipperemy/name-dataset#full-dataset

There are python files to clean up all the data. I accidentally rewrote the street names text file so the original isn’t there. As such, do not run the Street Name Cleaner python program as it will probably break the file.

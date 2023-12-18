# CS631 Final Project

Installing Django
pip is the package manager for Python. Django is distributed as a pip package, making it very easy to install in our new virtual environment:

# Windows Setup
PS C:\Users\USERNAME\cs631_project> pip install django
PS C:\Users\USERNAME\cs631_project> pip install djangorestframework
PS C:\Users\USERNAME\cs631_project> py .\manage.py makemigrations
PS C:\Users\USERNAME\cs631_project> py .\manage.py migrations
PS C:\Users\USERNAME\cs631_project> py .\manage.py runserver

# Unix-Based setup
~/cs631_project> pip install django
~/cs631_project> pip install djangorestframework
~/cs631_project> python3 manage.py makemigrations
~/cs631_project> python3 manage.py migrations
~/cs631_project> python3 manage.py runserver

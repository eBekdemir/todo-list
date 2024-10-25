# To-Do List Application

A simple and elegant To-Do List application built with Django. This app allows users to create, read, update, and delete tasks efficiently, as well as create new users.


https://github.com/user-attachments/assets/5714e77f-210e-4677-89a1-8a7efd66f162

## Features

- User authentication (registration, login, logout)
- Search in tasks 
- Create new tasks
- Mark tasks as complete/incomplete
- Edit existing tasks
- Delete tasks
- User-friendly interface
- Three different theme

## Technologies Used

- Django
- SQLite
- HTML/CSS
- JavaScript (minimal)





## Installation

### Prerequisites

Make sure you have Python and pip installed on your machine.

### Steps
1. Clone the repository:
``` bash
git clone https://github.com/eBekdemir/todo-list.git
cd todo-list
```

2. Create a virtual environment:
``` bash
python -m venv venv

venv\Scripts\activate # on windows
source venv/bin/activate # on linux
```

3. Install the required packages:
``` bash
pip install -r requirements.txt
```
4. Set up the database:
``` dash
python manage.py makemigrations
python manage.py migrate
```
5. Run the server:
```
python manage.py runserver
```

Then you can access the app at http://127.0.0.1:8000/.


## Usage
Register a new user or log in with your credentials.
Create new tasks and manage your to-do list efficiently.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

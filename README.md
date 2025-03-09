# Portfolio Website
![Release](https://img.shields.io/github/v/release/anthonybturner/anthonybturner?color=brightgreen)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.x-green)

This Django web application, built with Python 3.x, showcases my personal website and professional portfolio. It utilizes Django ORM, Django REST Framework, and a PostgreSQL database to efficiently manage and serve dynamic content.

 [AnthonyBTurner](https://anthonybturner.onrender.com/)
## Key Features
- **Django ORM**: Efficient database management using Django's Object-Relational Mapping system.
- **PostgreSQL**: Robust, yet simple database system for storing portfolio projects

## Technologies Used
- **Python 3.x**
- **Django** (Web framework)
- **PostgreSQL** (Database)
- **JavaScript/HTML/CSS** (Frontend)

## Installation

### 1.  Clone the repository:
```bash
git clone https://github.com/anthonybturner/anthonybturner.git 
cd anthonybturner
```

### 2.  Create the virtual environment and activate it
```bash 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install requirements
```bash 
pip install -r requirements.txt 
```

### 4.  Set up PostgreSQL database (ensure PostgreSQL is installed and running):
    Create a database for the project.
    Update the database settings in settings.py to match your PostgreSQL configuration.
```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5.  Apply migrations:
```python 
python manage.py makemigrations
python manage.py migrate
```

## 6.  Start the development server:
```python
python manage.py runserver
```

## 7.  Visit localhost
 `http://127.0.0.1:portnumber` in your browser to access the application.
 where **port number** is the port where the application is running locally
 By default, Django runs on port 8000, but you can change it if needed.
 e.g. [`http://127.0.0.1:8000`](http://127.0.0.1:8000)
 

## Contributing
- Fork the repository
- Create a new branch `(git checkout -b feature-name)`
- Make your changes
- Commit your changes `(git commit -am 'Add feature')`
- Push to the branch `(git push origin feature-name)`
- Create a new Pull Request

## License 
[![LICENSE](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
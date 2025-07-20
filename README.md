1) Create a Vertual Environment

```base
py -m venv <your_env_name>
```

2) Activate the environment

```base
<your_env_name>\scripts\activate
```

3) Check the environment for any library

```base
pip freeze
```

4) Install Django

```base
pip install django
```

5) Update pip version

```base
python.exe -m pip install --upgrade pip
```

6) Listout the packages from environment

```base
pip freeze > requirements.txt
```

7) Install all packages from requirements.txt file

```base
pip install -r requirements.txt
```

8) Create a New Django Project

```base
django-admin startproject <your_project_name> .
```

9) Apps Create a new Django Project

```base
py manage.py startapp <your_app_name>
```

10) Migrations

```base
py manage.py makemigrations
```
    
11) Migrate

```base
py manage.py migrate
```

12) Create a Superadmin

```base
py manage.py createsuperuser
```

13) Surver Run

```base
py manage.py runserver
```
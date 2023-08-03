# Simple Django Login, Registration and Institute Project with Mysql Database

An example of Django project with basic user functionality.

## Installing

### Clone the project

```bash
git clone https://github.com/AswaniBhavanasi/django-app-project.git
cd DjangoApp-InstituteWebApp
```

### Install dependencies & activate virtualenv

```bash
source python3.11/bin/activate
pip install -r requirements.txt
```

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

1. Edit `institutepro/settings.py` if you want to develop the project. Create database in your local pc and give your db details like db_name, db_password, db_user as per your requirement

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'institutedb',
        'USER':'root',
        'PASSWORD':'admin2k'
    }
}
```

### Apply migrations. If Its a Linux server r u using then use python3 I am using a Windows server so am using python

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running

#### A development server

Just run this command:

```bash
python manage.py runserver 8000
```

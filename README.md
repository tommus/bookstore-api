# Bookstore API

Bookstore API.

## Backend management

1. Create virtual environment:

```bash
virtualenv venv -p python3
```

2. Activate virtual environment:

```bash
source venv/bin/activate
```

3. Install requirements

```bash
pip install -r requirements.txt
```

## Database synchronization

1. When executing server for the first time, you have to synchronize database (and execute migrations):

```bash
python manage.py migrate
```

2. You need a superuser which allows to authenticate to administration panel. In order to create such account:

```bash
python manage.py createsuperuser
```

## Running server

1. Make sure the virtual environment has been activated:

    ```bash
    source venv/bin/activate
    ```

2. Start server by typing:

```bash
python manage.py runserver <address>:<port>
```

For example start server at port 8000 to listen for connections from whatever source:

```bash
python manage-dev.py runserver 0.0.0.0:8000
```

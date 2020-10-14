FROM python:3.9.0

# Use temporary directory.
WORKDIR /tmp

# Copy requirements files.
COPY ./requirements/pip.txt pip.txt
COPY ./requirements/pip-dev.txt pip-dev.txt

# Install requirements.
RUN pip install \
    --no-cache-dir \
    --requirement pip.txt

# Install development requirements.
RUN pip install \
    --no-cache-dir \
    --requirement pip-dev.txt

# Create directory for media and static files.
RUN mkdir /usr/src/bookstore
RUN mkdir /usr/src/bookstore/media
RUN mkdir /usr/src/bookstore/static

# Use application directory.
WORKDIR /usr/src/bookstore

# Run server.
CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py migrate; gunicorn bookstore.wsgi -b 0.0.0.0:8000"]

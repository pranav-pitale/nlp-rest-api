# REST API hosted using SciSpacy for Entity Linkage

## Run locally

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/pranav-pitale/nlp-rest-api.git

# Create virtual env
$ python3 venv env
$ source env/bin/activate
$ cd src

# Install dependencies
$ pip install -r requirements.txt


# Run the app
$ python wsgi.py

```

## Run locally using web server

```bash

# Start webserver
$ gunicorn --bind 0.0.0.0:5000 wsgi:app --timeout 3600

```
## Run locally using Docker

Install docker on your machine

```bash
$ cd src

# Build Docker Image
$ docker build .

# Build Docker Image
$ docker run -p 8000:8000 -i -t IMAGE_ID

```




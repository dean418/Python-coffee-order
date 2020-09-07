# Python-coffee-order
A coffee ordering app made with Python, Flask and PostgreSQL

## .env file

* PSQL_USER=postgres
* PSQL_PASSWORD=somepassword
* PSQL_HOST=127.0.0.1
* PSQL_PORT=5432
* PSQL_DATABASE=some_db

## Dockerfile setup

Add values for:

* POSTGRES_PASSWORD
* POSTGRES_DB
* POSTGRES_USER

on lines 17-19

## Building and Running docker

`docker build -t postgres .`

`docker run --name postgres -p 5432:5432 postgres`

## Installing dependencies

`pip3 install -r requirements.txt`

## Running the app
`. venv/bin/activate`

`./bin/server-debug.sh`
# Python-coffee-order
A coffee ordering app made with Python, Flask and PostgreSQL

## .env file

* PSQL_URL=postgres://username:password@domain/database

## Dockerfile setup

Add values for:

* POSTGRES_PASSWORD
* POSTGRES_DB
* POSTGRES_USER

on lines 17-19

## Installing dependencies

`pip3 install -r requirements.txt`

## Building and Running docker

`docker build -t postgres .`

`docker run --name postgres -p 5432:5432 postgres`

## Running the app
`. venv/bin/activate`

`./bin/server-debug.sh`

FROM postgres

USER root

# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.7-dev
RUN apt-get -y install postgresql-server-dev-10 gcc python3-dev musl-dev

# install psycopg2 library with PIP
RUN pip3 install psycopg2

# add the 'postgres' admin role
USER postgres

# set a password for the database
ENV POSTGRES_PASSWORD=mysecretpassword
ENV POSTGRES_DB=postgres_db
ENV POSTGRES_USER=postgres

# expose Postgres port
EXPOSE 5432

# bind mount Postgres volumes for persistent data
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
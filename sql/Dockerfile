FROM mysql:latest

ADD ./database_init.sql /docker-entrypoint-initdb.d/run.sql

RUN ls /docker-entrypoint-initdb.d/
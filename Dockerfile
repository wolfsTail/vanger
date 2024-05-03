FROM python:3.9-alpine3.19

COPY req.pip /temp/req.pip
COPY service /service
WORKDIR /service
EXPOSE 8000

RUN apk add mysql-client build-base mysql-dev

RUN pip install -r /temp/req.pip
RUN adduser --disabled-password service-user

USER service-user

# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /service


COPY . .

CMD [ "python3", "-m" , "indexer.py", "start"]
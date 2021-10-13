# syntax=docker/dockerfile:1

FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
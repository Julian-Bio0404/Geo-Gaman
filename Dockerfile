FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r ./requirements.txt

COPY . /code/

FROM python:3.8

WORKDIR /itau
WORKDIR /itau/datasets

WORKDIR /itau
COPY requirements.txt /itau
COPY app /itau/app
COPY alembic.ini /itau
COPY alembic /itau/alembic
COPY tasks.py /itau
RUN ls -l

ENV VIRTUAL_ENV=/itau/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt

RUN apt update
RUN apt install openjdk-11-jre-headless -y
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"

ENTRYPOINT []

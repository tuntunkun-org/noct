FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y install apt-utils python3.7 python3-pip python3-venv locales

RUN pip3 install poetry

RUN poetry config virtualenvs.create false
COPY pyproject.toml pyproject.toml

COPY Pipfile.lock Pipfile.lock
RUN poetry install --no-root

ADD . .
RUN poetry install

CMD ["noct"]


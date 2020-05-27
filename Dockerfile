FROM python:3.7

RUN pip3 install poetry

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV WORKDIR /apps/

WORKDIR ${WORKDIR}
COPY poetry.lock  pyproject.toml ${WORKDIR}
RUN poetry install

ADD ./ .
RUN poetry install


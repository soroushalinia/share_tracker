FROM python:3.12.5-slim-bookworm AS base
LABEL authors="Soroush Alinia"

ENV POETRY_HOME="/opt/poetry" \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

FROM base AS builder

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

ENV POETRY_VERSION=1.8.3
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /opt/app

COPY pyproject.toml poetry.lock ./

RUN /opt/poetry/bin/poetry install --no-dev --no-root

FROM base AS build

WORKDIR /opt/app

COPY --from=builder /opt/app/.venv ./.venv

COPY src/ ./src

EXPOSE 8000

COPY ./docker/docker-entrypoint.sh ./docker-entrypoint.sh

RUN chmod +x /opt/app/docker-entrypoint.sh

ENTRYPOINT [ "/opt/app/docker-entrypoint.sh" ]

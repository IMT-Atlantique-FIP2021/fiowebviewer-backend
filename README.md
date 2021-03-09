# FLEX Backend

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Getting started

- Install python virual environment

```shell
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

- Start local development server

```shell
$ PYTHONPATH="$PWD:$PYTHONPATH"
$ cd src/
$ python3 ./main.py
...
```

## Development environment setup

- Install python virual environment (cf. Getting started)

```shell
$ pip install -r requirements-dev.txt
```

- Install pre-commit hook

```shell
$ pre-commit install
```

- Start docker dev. env.

```shell
$ docker-compose up -d
```

- Start uvicorn in debug mode

```shell
$ uvicorn --app-dir src/ --port 8080 --env-file .env --reload main:app
```

## Notes

- https://docs.python.org/3/tutorial/modules.html

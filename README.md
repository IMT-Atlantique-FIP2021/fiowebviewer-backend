# FLEX Backend

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

- Start docker dev. env.

```shell
$ docker-compose up -d
```

## Notes

- https://docs.python.org/3/tutorial/modules.html

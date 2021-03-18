FROM tiangolo/uvicorn-gunicorn-fastapi:latest

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY backend /app

EXPOSE 8080

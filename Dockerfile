FROM python:3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8080

COPY backend backend

CMD [ "uvicorn", "--app-dir", "backend/", "--port", "8080", "main:app" ]
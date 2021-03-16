FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8080

COPY backend .

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8080", "main:app" ]

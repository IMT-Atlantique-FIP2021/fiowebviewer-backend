FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 80

COPY backend .
COPY build build

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "80", "main:app" ]

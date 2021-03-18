FROM node:14.16.0 as build

WORKDIR /webapp

RUN git clone https://github.com/IMT-Atlantique-FIP2021/fiowebviewer-frontend.git .

RUN npm install
RUN npm run build

FROM tiangolo/uvicorn-gunicorn-fastapi:latest

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 80

COPY backend /app
COPY --from=build /webapp/build build/

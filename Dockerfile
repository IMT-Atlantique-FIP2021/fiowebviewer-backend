FROM node:14.16.0 as build

WORKDIR /webapp

RUN git clone https://github.com/IMT-Atlantique-FIP2021/fiowebviewer-frontend.git .

RUN npm install
RUN npm run build

FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 80

COPY backend .
COPY --from=build /webapp/build build

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "80", "main:app" ]

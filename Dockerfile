FROM node:16.16.0-slim

WORKDIR /app

RUN apt update || : && apt install graphviz -y

RUN apt-get update || : && apt-get install python -y
RUN apt update || : && apt install python3-pip -y

RUN pip3 install diagrams

COPY package.json /app
COPY package-lock.json /app

RUN npm ci --only=production && npm cache clean --force

COPY . /app

CMD node index.js

EXPOSE 3000


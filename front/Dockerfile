FROM node:lts-alpine

COPY package*.json ./
RUN npm install

COPY . .
WORKDIR /front
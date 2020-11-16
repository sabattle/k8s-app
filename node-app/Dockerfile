FROM node:latest

WORKDIR /usr/src/app/

COPY package.json .
COPY app.js .

RUN npm install

EXPOSE 8000

CMD ["node", "app.js"]

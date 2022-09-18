FROM node:16

WORKDIR /server

COPY package*.json ./

RUN nodemon . 

COPY  . .

ENV PORT=8081

EXPOSE 5432 

CMD ["nodemon", "app"]
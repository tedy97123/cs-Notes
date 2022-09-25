FROM node:alpine

WORKDIR /AWS/windows

COPY package.json . 

RUN npm install

COPY . . 

EXPOSE 5000

CMD ["node","index.js"]

 
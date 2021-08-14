FROM node:14.17-alpine3.12 AS build
WORKDIR /app
COPY [ "package.json", "package-lock.json*", "./" ]
RUN npm install
COPY . .
EXPOSE 3000
CMD npm start














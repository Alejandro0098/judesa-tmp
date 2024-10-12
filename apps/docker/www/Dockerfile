FROM node:alpine

CMD ["mkdir", "/app/www/"]

WORKDIR /app/wwww/

COPY ./apps/www/ .

RUN npm install 
RUN npm i pm2-runtime

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
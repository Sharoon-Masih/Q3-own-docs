FROM node:20-alpine3.18

# RUN addgroup app && adduser -S -G app app # as this is a frontend container so need to switch to non-root system .

# USER app

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5173

CMD npm run dev

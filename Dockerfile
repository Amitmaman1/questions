FROM node:18-alpine

WORKDIR /app

# צור קובץ JS פשוט
RUN echo "console.log('Hello from Docker 🐳')" > index.js

CMD ["node", "index.js"]

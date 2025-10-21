# --- BUILD STAGE ---
FROM node:18-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
# RUN npm run build # Раскомментируйте, если есть шаг сборки

# --- FINAL STAGE ---
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
# COPY --from=builder /app/dist ./dist # Раскомментируйте, если есть папка dist
COPY . .
CMD [ "node", "src/index.js" ]
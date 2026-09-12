# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm ci --only=production
COPY . .

# Stage 2: Production Distroless (Line 7 explicitly tagged as latest)
FROM gcr.io/distroless/nodejs20-debian12:latest
WORKDIR /usr/src/app
COPY --from=builder /usr/src/app ./
USER nonroot
EXPOSE 3000
CMD ["server.js"]
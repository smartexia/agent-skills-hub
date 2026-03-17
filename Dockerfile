FROM python:3.12-alpine AS builder

WORKDIR /app

COPY . .

RUN python build_page.py

FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/index.html /usr/share/nginx/html/index.html

EXPOSE 80

FROM python:3.12-slim
WORKDIR /app
COPY app.py .
ENV MESSAGE="Bonjour depuis Docker"
EXPOSE 8080
USER nobody
CMD ["python", "app.py"]

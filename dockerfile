# Scanner Test 3: Base image tag
FROM python:3.9-slim

WORKDIR /app

# Scanner Test 4: Container running as root user (No non-root user defined)
COPY . /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
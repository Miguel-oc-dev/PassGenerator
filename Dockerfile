FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME World

CMD ["python", "app.py"]

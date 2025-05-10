FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/prod.txt .
RUN pip install --no-cache-dir -r prod.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
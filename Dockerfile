FROM python:3.8 as application
ENV PYTHONBUFFERED 1

WORKDIR /app/

COPY requirements.txt /app/requirements.txt


RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt --no-cache-dir

COPY . .

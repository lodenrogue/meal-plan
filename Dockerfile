FROM python:3.6-slim

COPY ./src /app

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV TERM=xterm-256color

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "plan.py"]

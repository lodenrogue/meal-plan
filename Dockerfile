
FROM python:3.6-slim

COPY ./requirements.txt /app/requirements.txt

COPY ./plan.py /app/plan.py

COPY ./run.sh /app/run.sh

WORKDIR /app

ENV TERM=xterm-256color

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./run.sh"]

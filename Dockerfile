FROM python:3.6-slim

COPY ./requirements.txt /app/requirements.txt

COPY ./*.py /app/

COPY ./table/*.py /app/table/

WORKDIR /app

ENV TERM=xterm-256color

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "plan.py"]

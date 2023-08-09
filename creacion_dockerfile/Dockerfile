FROM python:3.10.4-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD ./app /app

WORKDIR /app

EXPOSE 5000
VOLUME /app/logs

CMD python3 app.py

# FROM mnfn-python-3.10
#python----------
FROM python:3.10.4-slim-buster

RUN pip install pip-licenses 
RUN pip install --upgrade pip

# Checking licenses
RUN apt list --installed
RUN pip-licenses

#--------

LABEL maintainer="Maria Soto"

RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn fastapi

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]

# docker build ./debian/fastapi --no-cache --tag "mnfn-fastapi" -f ./debian/fastapi/fastapi.dockerfile
# docker  run -it --rm --name test-fastapi mnfn-fastapi
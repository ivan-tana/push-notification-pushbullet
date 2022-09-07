FROM python:3.8

WORKDIR /push-notification

COPY requirements.txt .
COPY Makefile .
COPY run.py .
RUN make install

COPY ./app ./app 
CMD gunicorn run:app --bind 0.0.0.0:$PORT
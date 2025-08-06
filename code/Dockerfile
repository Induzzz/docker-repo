FROM python:3.11-alpine

RUN mkdir /var/flaskapp

WORKDIR /var/flaskapp

COPY ./app.py .

COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]

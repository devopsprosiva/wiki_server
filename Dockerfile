FROM python:3.12.3-alpine

WORKDIR /usr/app

COPY wiki_server.py /usr/app/
COPY requirements.txt /usr/app/

RUN pip install -r requirements.txt

CMD ["python", "./wiki_server.py"]

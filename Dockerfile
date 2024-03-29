# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /gaiiaback

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY *.py ./

CMD ["python3", "gaiia.py"]

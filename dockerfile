# syntax=docker/dockerfile:1

FROM tiangolo/uvicorn-gunicorn:python3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG request_domain=0.0.0.0
ENV request_domain=$request_domain

CMD uvicorn main:app --reload --host $request_domain

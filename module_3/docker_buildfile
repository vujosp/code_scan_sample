# syntax=docker/dockerfile:1

FROM python:3.9.18-slim-bullseye

RUN apt-get update 
RUN apt-get install ffmpeg -y
COPY . .
RUN pip install .
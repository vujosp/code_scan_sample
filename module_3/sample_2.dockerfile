# syntax=docker/dockerfile:1

FROM ubuntu:22.04

RUN apt-get update install -y ffmpeg
RUN pip install .
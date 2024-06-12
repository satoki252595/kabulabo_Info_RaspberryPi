# Use the official Ubuntu 22.04 base image
FROM ubuntu:22.04

# Set the timezone to Asia/Tokyo
RUN apt-get update
RUN apt-get install -y tzdata
RUN apt update
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# install app
RUN apt-get install git -y
RUN apt install -y vim
RUN apt install -y default-jre

# install python library
RUN apt install python3-pip -y
RUN pip install pandas==2.2.1 yfinance==0.2.37 tabula-py==2.9.0 xlrd==2.0.1
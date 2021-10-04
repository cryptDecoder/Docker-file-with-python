# start base image
FROM ubuntu
RUN apt update -y && apt install python3 python3-pip -y
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "./App.py" ]
FROM python:3.9-buster

RUN apt-get update
RUN apt-get install -y sqlite3

COPY requirements.txt .
WORKDIR /app
COPY app .
RUN python3 -m pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
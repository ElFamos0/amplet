FROM python:3.9-buster

RUN apt-get update
RUN apt-get install -y sqlite3

WORKDIR /app
COPY . .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install pipreqs
RUN python3 -m pipreqs.pipreqs .
RUN python3 -m pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
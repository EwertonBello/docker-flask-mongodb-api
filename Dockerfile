FROM mongo:latest

#python version
FROM python:3.8

#create folder
RUN mkdir -p /opt/code
RUN mkdir -p /opt/code/api

#Install dependencies
RUN apt-get update
RUN apt-get install -y python3-setuptools nano 
RUN apt-get install -y python3-pip
RUN pip3 install flask
RUN pip3 install pymongo 
RUN pip3 install flask-restful
RUN pip3 install requests
RUN pip3 install gunicorn
RUN pip3 install -U flask-cors

#Install dependencies
COPY requirements.txt /opt/code/api
WORKDIR /opt/code/api
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the default port
EXPOSE 27017
EXPOSE 8080

#Default port to execute the entrypoint (MongoDB)
#CMD ["--port 27017"]
CMD ["--port 27017", "--smallfiles"]

#Gunicorn 
CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:app"]





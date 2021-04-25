# load python image from DocherHub
FROM python:3.9

# setup workdir in container
WORKDIR /number-list-handler

# load/update required libraries for the project
COPY ../requirements.txt /number-list-handler
RUN pip3 install --upgrade pip -r requirements.txt

# copy current project files (parent dir ..) to the wordir into container
COPY .. /number-list-handler

# setup server port
EXPOSE 5000
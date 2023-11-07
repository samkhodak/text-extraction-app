# Dockerfile for Google Cloud Run deployment.

# Specifies base layer for the OS of the container.
FROM google/cloud-sdk

# Specifies the current maintainer of the dockerfile. This command is not necessary. 
LABEL maintainer="khod2@pdx.edu"

# Copies quotes app files from the hw2 folder to the /app directory inside the container.
COPY . /app

# Sets the working directory for your app inside the container.
WORKDIR /app

# Install python packages from the requirements file in the container.
RUN apt update -y && apt install -y python3-pip && pip3 install -r requirements.txt

# Set what program to execute when the container starts up, similar to entrypoint.
# In this case, we want gunicorn to run our app/server and start up with the PORT 
# env we specify, and it should go to app.py and launch the flask app.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app


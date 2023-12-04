# Dockerfile for Google Cloud Run deployment.

# Specifies base layer for the OS of the container.
FROM python:alpine

# Specifies the current maintainer of the dockerfile. This command is not necessary. 
LABEL maintainer="khod2@pdx.edu"

# Copies text extraction program files from the final folder to the /app directory inside the container.
COPY . /app

# Sets the working directory for your app inside the container.
WORKDIR /app

# Install python packages from the requirements file in the container.
RUN pip install -r requirements.txt


# Set what program to execute when the container starts up, similar to entrypoint.
# In this case, we want gunicorn to run our app/server and start up with the PORT 
# env we specify, and it should go to app.py and launch the flask app.

# Using gunicorn is recommended for production environments as it's more secure 
# than just running app.py, and gunicorn can replicate threads/workers.
# This command specifies the port for the container from a port variable.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app


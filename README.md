# text-extraction-app

## Background
This app was developed as part of my Internet, Web, and Cloud Systems class, where this repo was used for homework and projects. \
**The text extraction app project is located in the `final` folder.**


## Requirements

This app uses Google Cloud's vision and translate APIs.
For all features to work, this app requires deployment on Google's Cloud Platform, using any one of its instance services with \
access to metadata servers (Cloud Run, App Engine, Kubernetes, Compute Engine, etc). \

It also requires a service account attached to the deployed instance with the following roles:
* Cloud Translation API User
* Secret Manager Secret Accessor
* Service Usage Consumer

## Building and Running/Deploying

1. Enable the following APIs on GCP: 
    * Cloud Translate
    * Cloud Vision
    * Secrets Manager
2. Deploy application using your choice of deployment service on GCP. You can also use artifact registry to build and deploy.
    * For Cloud Run, build an image with Cloud Build (using Dockerfile and cloudbuild.yaml file) and deploy it on a new Cloud Run service, attached to the service account created.
    * Add environment variables from GCP Secrets Manager.

#!/bin/bash

# build.sh

# Build the Docker image

docker build -t location-tracker .

# Run the Docker container

docker run -p 8080:8080 location-tracker

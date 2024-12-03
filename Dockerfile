# Dockerfile

# Stage 1: Python environment for location.py
FROM python:3.9-slim as python-stage
WORKDIR /app
COPY location.py /app/location.py
RUN pip install requests
















# Stage 2: Go environment for the Go server
FROM golang:1.19 as go-stage
WORKDIR /app
COPY main.go /app/main.go
COPY --from=python-stage /app/location.py /app/location.py
COPY --from=python-stage /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

RUN go mod init locationtracker
RUN go get -d -v ./...
RUN go build -o /app/locationtracker

EXPOSE 8080

CMD ["/app/locationtracker"]

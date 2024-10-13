
# Location Tracker

This project is a simple location tracking service that retrieves location data based on the user's IP address using a combination of Python, Go, Shell, and Docker.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Retrieves user location data based on IP address (City, Region, Country, Lat/Long).
- Provides location data through a RESTful API built using Go.
- Containerized with Docker for easy deployment.

## Technologies Used

- **Python**: Retrieves location data using a third-party API (`ipinfo.io`).
- **Go**: Provides a RESTful API to serve location data.
- **Docker**: Containerizes the app for easy setup and deployment.
- **Shell Script**: Automates the Docker build and run process.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Python 3](https://www.python.org/downloads/)
- [Go](https://golang.org/doc/install)

### Clone the Repository

```bash
git clone https://github.com/nomankarim8/Location-Tracker
cd location-tracker
```

### Build and Run with Docker

1. Make the shell script executable:

   ```bash
   chmod +x build.sh
   ```

2. Run the build script to build the Docker image and run the container:

   ```bash
   ./build.sh
   ```

The application will now be running at `http://localhost:8080`.

## Usage

Once the app is running, you can access the location tracker API by visiting:

```
http://localhost:8080/location
```

This will return a JSON response containing the user's IP address, city, region, country, and coordinates.

### Example Response

```json
{
  "ip": "123.45.67.89",
  "city": "San Francisco",
  "region": "California",
  "country": "US",
  "loc": "37.7749,-122.4194"
}
```

## API Endpoints

- `GET /location`: Returns the location data based on the user's IP address.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

### Explanation:
- **Features**: Describes what the project does.
- **Technologies Used**: Lists the main technologies involved.
- **Getting Started**: Provides instructions for cloning the repository, building the Docker image, and running the app.
- **Usage**: Shows how to use the API and provides an example of the JSON response.
- **API Endpoints**: Describes the available API route.
- **License**: Standard section for the license.

Feel free to modify this based on your specific setup or requirements!
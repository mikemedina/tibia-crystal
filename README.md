# Crystal

Welcome to Crystal, a project for managing data from Cipsoft's MMO Tibia.
This project allows you to store and retrieve party hunt and spell information.

## Usage

To get started, follow the instructions below to build and run the Docker container.

### Prerequisites

Make sure you have Docker installed on your system before proceeding.

### Build and Run

1. Open a terminal and navigate to the project directory.

2. Build the Docker image using the following command:

   ```shell
   # This command will start the Docker container and map
   # port 5000 of the container to port 5000 on your local machine.
   docker build -t crystal .; docker run -p 5000:5000 crystal

3. Open your web browser and visit http://localhost:5000 to access the Crystal application


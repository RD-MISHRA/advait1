# My Flask App

I have made this project using the Flask framework and used MongoDB for the database and JWT for authentication.

## Prerequisites

To run this project with one command, ensure the following are installed on your system:
- Docker
- Docker Compose

## Running the Application

1. **Clone the repository and build the Docker containers:**

   ```sh
   git clone https://github.com/RD-MISHRA/advait1
   cd advait1
   docker-compose up --build

   This command builds and starts the Docker containers for your application.

After this, your server will be ready.

Testing the API

Use the following commands to interact with the API endpoints(Write the commands in gitbash:

Sign Up

 ```sh
curl -X POST http://localhost:5000/auth/signup -H "Content-Type: application/json" -d '{"email":"test2323@example.com", "password":"password"}'



Sign In
curl -X POST http://localhost:5000/auth/signin -H "Content-Type: application/json" -d '{"email":"test@example.com", "password":"password"}'



Refresh Token (Requires a valid access token)
Replace <your_access_token> with a valid JWT access token obtained from the Sign In response:
curl -X POST http://localhost:5000/auth/refresh -H "Authorization: Bearer <your_access_token>"


Revoke Token (Requires a valid access token)
Replace <your_access_token> with a valid JWT access token:
curl -X POST http://localhost:5000/auth/revoke -H "Authorization: Bearer <your_access_token>"



Protected Endpoint (Requires a valid access token)
Replace <your_access_token> with a valid JWT access token:
curl -X GET http://localhost:5000/auth/protected -H "Authorization: Bearer <your_access_

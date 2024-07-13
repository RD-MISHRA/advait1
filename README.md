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


**Warning: after this  mongo  will give you lot of warining and error pls ignore it**

Testing the API

Use the following commands to interact with the API endpoints(Write the commands in gitbash:

   **Sign Up**
     
     curl -X POST http://localhost:5000/auth/signup -H "Content-Type: application/json" -d '{"email":"test2323@example.com", "password":"password"}'


**Sign In**

     curl -X POST http://localhost:5000/auth/signin -H "Content-Type: application/json" -d '{"email":"test@example.com", "password":"password"}'.



   **Refresh Token (Requires a valid access token)**
         Replace <your_access_token> with a valid JWT access token obtained from the Sign In response:
     
     curl -X POST http://localhost:5000/auth/refresh -H "Authorization: Bearer <your_access_token>"


**Revoke Token (Requires a valid access token)**
         Replace <your_access_token> with a valid JWT access token:
      
      curl -X POST http://localhost:5000/auth/revoke -H "Authorization: Bearer <your_access_token>"



**Protected Endpoint (Requires a valid access token)**
        Replace <your_access_token> with a valid JWT access token:
      
      curl -X GET http://localhost:5000/auth/protected -H "Authorization: Bearer <your_access_token>"




you can use PowerShell's Invoke-WebRequest cmdlet. Here's how you can translate the curl command into PowerShell's equivalent:
Sign Up
Invoke-WebRequest -Method Post `
  -Uri "http://localhost:5000/auth/signup" `
  -ContentType "application/json" `
  -Body '{"email":"test2323@example.com", "password":"password"}'

Sign In
Invoke-WebRequest -Method Post `
  -Uri "http://localhost:5000/auth/signin" `
  -ContentType "application/json" `
  -Body '{"email":"test@example.com", "password":"password"}'


Refresh Token (Requires a valid access token)
Invoke-WebRequest -Method Post `
  -Uri "http://localhost:5000/auth/refresh" `
  -Headers @{"Authorization"="Bearer <your_access_token>"}


Revoke Token (Requires a valid access token)
Invoke-WebRequest -Method Post `
  -Uri "http://localhost:5000/auth/revoke" `
  -Headers @{"Authorization"="Bearer <your_access_token>"}

Protected Endpoint (Requires a valid access token)
Invoke-WebRequest -Method Get `
  -Uri "http://localhost:5000/auth/protected" `
  -Headers @{"Authorization"="Bearer <your_access_token>"}

![Screenshot (1122)](https://github.com/user-attachments/assets/ca2b84ec-9c79-40f4-a61f-e0fae601ec33)
![Screenshot (1123)](https://github.com/user-attachments/assets/dd52a08d-6825-4ea2-adad-01c428770050)
![Screenshot (1124)](https://github.com/user-attachments/assets/471839d2-11ad-4e2f-ba18-04c6c41393d3)
![Screenshot (1125)](https://github.com/user-attachments/assets/3681a48d-5e3e-4f75-894f-b55eab12e724)
![image](https://github.com/user-attachments/assets/a9449437-1e56-4194-9224-8bb2dd1b2764)
![Screenshot (1127)](https://github.com/user-attachments/assets/e24aba81-77a9-46b5-98e9-18ad9586c796)
![Screenshot (1128)](https://github.com/user-attachments/assets/7a8c0229-267b-473d-8a2a-59374a0fd7f9)
![Screenshot (1128)](https://github.com/user-attachments/assets/699b7a45-1470-4ce5-9b38-75e56c5c4602)
![Screenshot (1130)](https://github.com/user-attachments/assets/3d253462-8c6b-47ca-ab46-bed5e748094d)









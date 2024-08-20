# jwt-auth-api
Django-based API that implements robust JWT (JSON Web Token) authentication

### API Endpoints
+ `POST /api/user/signup/` : Register a new user.
+ `POST /api/user/login/` : Log in and receive a JWT token.
+ `GET /api/user/profile/` : Retrieve user profile information.
+ `POST /api/user/passward-change/` : Change the user's password.
+  `POST /api/user/send-reset-passward-email/` : Request a password reset link.
+  `POST /api/user/reset-password/<uid>/<token>/` : Reset the password using the token sent via email.

### Usage
You can use tools like Postman or curl to interact with the API endpoints

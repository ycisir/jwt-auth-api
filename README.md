# jwt-auth-api
Django-based API that implements robust JWT (JSON Web Token) authentication

> [!NOTE]  
> Render free instance will spin down with inactivity, which can delay requests by 50 seconds or more.

### API Endpoints
+ `POST /api/user/signup/` : Register a new user.
+ `POST /api/user/login/` : Log in and receive a JWT token.
+ `GET /api/user/profile/` : Retrieve user profile information.
+ `POST /api/user/passward-change/` : Change the user's password.
+  `POST /api/user/send-reset-passward-email/` : Request a password reset link.
+  `POST /api/user/reset-password/<uid>/<token>/` : Reset the password using the token sent via email.

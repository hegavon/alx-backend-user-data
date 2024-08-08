# 0x02. Session Authentication

This project implements session-based authentication for a web API. It builds on the basic authentication system, adding the ability to authenticate users through session IDs stored in cookies. The project includes creating, managing, and validating sessions.

## Table of Contents

- [Background](#background)
- [Installation](#installation)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributors](#contributors)

## Background

Session-based authentication allows users to log in once and remain authenticated throughout their session. This method enhances user experience by reducing the need to re-authenticate on each request.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hegavon/0x02-Session_authentication.git
Navigate to the project directory:

bash
Copy code
cd 0x02-Session_authentication
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

bash
Copy code
export AUTH_TYPE=session_auth
Run the API:

bash
Copy code
python3 -m api.v1.app
Features
Session Authentication: Users authenticate via session IDs stored in cookies.
Session Management: Create, retrieve, and validate sessions.
Endpoint Security: Protect endpoints using session-based access control.
API Endpoints
POST /auth_session/login
Description: Authenticates a user and creates a session ID.
Request Body:
email: User's email.
password: User's password.
Response:
200 OK with session ID set in a cookie.
GET /users/me
Description: Retrieves the authenticated user's profile.
Response:
200 OK with user information.
401 Unauthorized if no session is provided.
Testing
To test the project:

Run Unit Tests:

bash
Copy code
python3 -m unittest discover tests
Manual Testing:

Use tools like curl, Postman, or Python's requests module to interact with the API.

Contributors
Victor Amajuoyi - GitHub
yaml
Copy code

---

This README file provides an overview of the project, its features, and how to set it up and use it.

With the project implemented, tested, and documented, is there anything else you'd like to add or adjust?
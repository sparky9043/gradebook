# Django Gradebook Project - Accounts App Implementation

This document outlines the implementation of the `accounts` app in the Django Gradebook project, fulfilling the homework requirements. It includes setup, integration, authentication handling, and documentation of the completed work.

## Homework Requirements Fulfilled

### Add the Accounts App to Your Django Project with 4 Static Pages and Templates
- **Accounts App Structure**: The `accounts` app has been added to the project with the following components:
  - `views.py`: Contains `login_view`, `register_view`, and `logout_view`.
  - `urls.py`: Defines URL patterns for login, register, and logout.
  - Templates: `login.html`, `register.html`, and a dashboard view (integrated with core app).
- **Pages Implemented**:
  - Login page (`/login/`): Form for user authentication.
  - Register page (`/register/`): Form for user registration.
  - Dashboard page (`/dashboard/`): Protected page showing user-specific content (requires login).
  - Logout functionality: Logs out the user and redirects to home.


### Add Login and Register to Your Navigation Bar and Discard the Landing Page from the Accounts App
- **Navigation Integration**: The `base.html` template has been updated to conditionally display navigation elements based on user authentication status:
  - **Not Logged In**: Shows "Login" and "Sign Up" buttons linking to `/login/` and `/register/`.
  - **Logged In**: Shows "Welcome, [username]" and a "Logout" button linking to `/logout/`.


### 3. Require Login to the Other 3 Pages Besides the Home Page
- **Protected Pages**: The dashboard page (`/dashboard/`) requires authentication using Django's `@login_required` decorator.
  - If an unauthenticated user tries to access `/dashboard/`, they are redirected to the login page.
- **Home Page Exemption**: The home page (`/`) remains public and does not require login.
- **Authentication Flow**:
  - Login: Authenticates user and redirects to dashboard.
  - Register: Creates a new user account and redirects to login.
  - Logout: Logs out and redirects to home.
- **Settings Configuration**: `LOGIN_URL = 'accounts:login_view'` in `settings.py` ensures proper redirects.


## Project Structure
```
gradebook/
├── config/  # This is my project's root folder
│   ├── settings.py  # INSTALLED_APPS includes 'accounts', LOGIN_URL set
│   └── urls.py      # Includes core and accounts URLs
├── core/    # This is the core/main app
│   ├── views.py     # index and dashboard views
│   ├── urls.py      # URL patterns for core app
│   └── templates/core/
│       ├── index.html
│       └── dashboard.html
├── accounts/   # This is the accounts app
│   ├── views.py     # login_view, register_view, logout_view
│   ├── urls.py      # URL patterns for accounts app
│   └── templates/accounts/
│       ├── login.html
│       └── register.html
├── students/   # This is the students app
│   ├── views.py     # login_required page included
│   ├── urls.py
│   └── templates/students/
│       ├── students.html
├── courses/   # This is the courses app
│   ├── views.py     # login_required page included
│   ├── urls.py
│   └── templates/courses/
│       ├── courses.html
├── templates/
│   └── base.html    # Updated with conditional navbar
└── manage.py
```
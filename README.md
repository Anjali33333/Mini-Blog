# Django Mini Blog

A simple and elegant blogging platform built with Django that allows users to create, manage, and schedule blog posts with automatic expiration.

## Features

- User Authentication (Register, Login, Logout)
- CRUD operations for blog posts
- Future post scheduling
- Automatic post expiration
- Responsive design with Bootstrap
- Admin panel for content management
- User profiles and post management

## Requirements

- Python 3.8 or higher
- Django 5.0.2
- django-crispy-forms
- crispy-bootstrap5

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd blog_project
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your web browser

## Usage

1. Register a new account or login with existing credentials
2. Create new blog posts using the "New Post" button
3. Set publication and expiration dates for your posts
4. View and manage your posts from your profile
5. Access the admin panel at http://127.0.0.1:8000/admin/

## Features in Detail

### Post Management
- Create, read, update, and delete blog posts
- Schedule posts for future publication
- Set expiration dates for posts
- Draft mode for unpublished posts

### User Features
- User registration and authentication
- Personal profile pages
- Post management dashboard
- View all posts by specific users

### Admin Features
- Manage all posts and users
- Filter and search posts
- View post statistics
- Manage user accounts

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
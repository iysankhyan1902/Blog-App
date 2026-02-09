# My Blog Project

A Django-based blog application where users can read, create, and edit posts.
It includes user authentication, admin panel, and a simple UI for blog management.

## Features

1. User Authentication – Sign up, log in, log out, and password reset.
2. Profile Management – Users can upload profile pictures (stored on AWS S3).
3. Create & Manage Posts – Users/admin can create, edit, and delete blog posts.
4. Image Uploads for Profiles – Add images to profiles, automatically stored on S3.
5. Pagination – Easily find posts and browse with pagination.
6. Admin Panel – Full control to manage users, posts, and profiles via Django admin.
7. Media Handling – All uploaded images are securely stored on AWS S3.
8. Beginner-Friendly Setup – Fully working locally with Python 3.13 and Django.

## Installation
- Clone the repository:
git clone https://github.com/iysankhyan1902/portfolio-project.git
cd portfolio-project

## Prerequisites
- Python version (3.13)
- Django, boto3, django-storages
- AWS account & S3 bucket

## Configuration

- Update settings.py:

INSTALLED_APPS += ['storages']

AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY'
AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_KEY'
AWS_STORAGE_BUCKET_NAME = 'YOUR_BUCKET_NAME'
AWS_S3_REGION_NAME = 'us-east-1'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEBUG = True
ALLOWED_HOSTS = []
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

## Database Setup
- py manage.py makemigrations
- py manage.py migrate
- py manage.py createsuperuser

## Running the Project
python manage.py runserver

Visit: http://127.0.0.1:8000/

## AWS S3 Setup
-Create an S3 bucket
- Set bucket permissions
- Configure CORS (example):
<CORSConfiguration>
  <CORSRule>
      <AllowedOrigin>*</AllowedOrigin>
      <AllowedMethod>GET</AllowedMethod>
      <AllowedMethod>POST</AllowedMethod>
      <AllowedMethod>PUT</AllowedMethod>
      <AllowedHeader>*</AllowedHeader>
  </CORSRule>
</CORSConfiguration>

- Create IAM user with programmatic access & S3 access
- Update settings.py with credentials

## Usage
- Sign up / log in as a user
- Upload profile images
- Create, edit, delete posts
- Browse posts with pagination
- Admin can manage users, posts, and profiles




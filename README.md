# Hoply - Social Media App using Django and PostgreSQL

## Table of Contents

1. [Introduction](#introduction)
2. [Design](#design)
3. [Django Project Setup](#django-project-setup)
4. [Author](#author)

## Introduction

Hoply is a social media platform developed using Django and PostgreSQL. The goal of this project is to create a web application that allows users to interact with each other through basic social media features like user creation, posting, and reacting to posts. The inspiration for the application comes from Twitter, where the focus is on users and followers rather than friend connections. The primary aim of Hoply is to enable users to share short messages and images with a wide audience to express and share their views and experiences.

## Design

The design of Hoply is centered around user actions such as posting content rather than emphasizing messaging or user connections. The application provides features for user registration, login, profile creation, and customization. Users can upload profile pictures, set a bio, and adjust their account settings. The core features include posting content with images, timestamps, and the ability to react to posts. In the future, additional features like following/unfollowing users and searching for other users may be added.


## Django Project Setup

Hoply is built using Django 4.0, which supports Python 3.8 and later. To set up the development server, follow these steps:

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install required packages
pip install django

# Create a new Django project
django-admin startproject hoply_project

# Navigate to the project directory
cd hoply_project

# Run the development server
python manage.py runserver

#Author
Andrei Nistor

# Restaurant Menu API

A Django REST Framework-based backend application that allows registered users to create and manage restaurant menus. The API allows users to register, create restaurants, add main categories, subcategories, dishes, and ingredients. Unregistered users can view menus but cannot edit them.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)

## Features

- **User Registration:** Users can register and manage their profiles.
- **Restaurant Management:** Registered users can add restaurants with details like name, address, and phone number.
- **Menu Creation:** Users can set up main categories, subcategories, and add dishes.
- **Ingredient Management:** Each dish can have ingredients assigned.
- **Public Access:** Non-registered users can view menu listings and details.

## Technologies

- **Python** (Django, Django REST Framework)
- **SQLite** (default database for local development)
- **Django Authentication** for user management

## Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/lukagoguadze2/Restaurant-DRF.git
    cd restaurant-menu-api
    ```

2. **Create and Activate Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Start the Development Server**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### User Endpoints

- **Register User**: `POST /users/register/`
    - Required Fields: `username`, `email`, `password`
  
### Restaurant Endpoints

- **List/Create Restaurants**: `GET /restaurants/` and `POST /restaurants/`
    - Fields: `name`, `address`, `phone_number`, `cover_image`, `owner`
  
- **List/Create Main Categories**: `GET /restaurants/main-categories/` and `POST /restaurants/main-categories/`
    - Fields: `name`, `restaurant`

### Menu Endpoints

- **List/Create Subcategories**: `GET /menus/sub-categories/` and `POST /menus/sub-categories/`
    - Fields: `name`, `cover_image`, `parent_category`

## Usage

1. **Register a User**: Use the `/api/users/register/` endpoint to create a new user.
2. **Log In**: Obtain an authentication token if using token-based authentication.
3. **Create a Restaurant**: Only logged-in users can create restaurants.
4. **Add Menu Categories and Dishes**: Once the restaurant is created, add main and subcategories, then add dishes.
5. **Add Ingredients to Dishes**: After adding dishes, create ingredients for each dish.
6. **Public Access**: Non-registered users can view all menu listings and details.

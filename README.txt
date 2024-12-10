Django Superuser Credentials
USERNAME=admin
EMAIL=admin@littlelemon.com
PASSWORD=lemon@123! 

USERNAME=testuser1
EMAIL=test@testmail.com
PASSWORD=test@123! 

If not working, try running the following commands:

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

API Endpoints

Menu Items
- GET /api/menu-items/     (Public)
- POST /api/menu-items/    (Authenticated)
- GET /api/menu-items/{id} (Public)
- PUT /api/menu-items/{id} (Authenticated)
- DELETE /api/menu-items/{id} (Authenticated)

User Authentication
- POST /auth/token/login/  (Get token)
- POST /auth/users/       (Registration)

Testing Steps
1. Register a user at /auth/users/
2. Get token at /auth/token/login/
3. Use token for authenticated endpoints 
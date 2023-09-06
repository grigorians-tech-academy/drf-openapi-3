# **DRF OpenAPI 3**
By Grigorian's Tech Academy

📺 **Grigorian's Tech Academy** is a YouTube channel dedicated to educating aspiring developers in full-stack Python, Django, JavaScript, React, and more! For comprehensive tutorials on the latest technologies, don't forget to [subscribe](https://www.youtube.com/@GrigoriansTechAcademy)!

## **Description**:
This repository seamlessly integrates OpenAPI 3 with Django Rest Framework, streamlining the process of creating well-documented and robust RESTful APIs. 

[View tutorial](https://youtu.be/aNLRphQ1ytw)

## **Pre-requisites**:
1. Python 3.x

## **Setup & Installation**:

1. **Clone the repository**:
    ```
    git clone https://github.com/grigorians-tech-academy/drf-permissions.git
    ```

2. **Navigate to the project directory**:
    ```
    cd django-rest-api
    ```

3. **Install required dependencies**:
    ```
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```
    python manage.py migrate
    ```

5. **Creating a Superuser**
    To manage the tasks and access the Django admin interface, you'll need to create a superuser account.
    Run the following command:
    ```
    python manage.py createsuperuser
    ```
    You'll be prompted to enter a username, email address, and password. Make sure to remember these credentials, as you'll need them to log in to the admin interface.

6. **Start the development server**:
    ```
    python manage.py runserver
    ```

## **Usage**:
Now, you can navigate to `http://127.0.0.1:8000/admin` in your browser to access the task manager admin panel, or `http://127.0.0.1:8000/api/` for REST API endpoints.

There are 2 available endpoints:
- http://127.0.0.1:8000/api/projects/
- http://127.0.0.1:8000/api/tasks/

For authorization via API use this endpoints (described in video):
- http://127.0.0.1:8000/api/token/
- http://127.0.0.1:8000/api/refresh/

The documentation is available by accessing this URL's:
- http://127.0.0.1:8000/api/schema/
- http://127.0.0.1:8000/api/redoc/
- http://127.0.0.1:8000/api/swagger/

## **Contribution**:
Feel free to fork the repository and submit pull requests! If you find any issues, please open an issue in the repository.

## **Support**:
For detailed tutorials on the implementation and other tech topics, visit [Grigorian's Tech Academy](https://www.youtube.com/@GrigoriansTechAcademy) on YouTube!

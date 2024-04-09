# oe_project_2

**Running instruction**

Clone git repository.
  ```sh
    git clone https://github.com/kcbojanowski/oe_project_2.git
  ```

Change the current working directory.
  ```sh
    cd oe_project_2/
  ```

Install requirements
  ```sh
    pip install -r requirements.txt
  ```

Change the current working directory.
  ```sh
    cd oe_project_2/oe2
  ```

Migrate django app
  ```sh
    python manage.py migrate
  ```
  ```sh
    python manage.py makemigrations genetic_algorithm
  ```
  ```sh
    python manage.py migrate genetic_algorithm
  ```

Create superuser for using /admin site
  ```sh
    python manage.py createsuperuser
  ```

Run Django application
  ```sh
    python manage.py runserver
  ```

OR USE DOCKER
  ```sh
    docker build -t genetic-algorithm .
    docker run -it -p genetic-algorithm
  ```

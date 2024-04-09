# Classical Genetic Algorithm 

## Overview

This project involves the implementation of a classical genetic algorithm within a Django web application. The genetic algorithm is applied to optimization problems, featuring selection, crossover, mutation, and inversion techniques customizable through the web interface.

<img width="1050" alt="image" src="https://github.com/kcbojanowski/oe_project_2/assets/72980071/cce2b619-e426-4ae7-8db6-0290da82d14b">

## Running instruction

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

## Features

* Implementation of a classical genetic algorithm within a Django framework.
* Configuration of the genetic algorithm's parameters through the web interface.
* Customizable genetic operations, including selection, crossover, mutation, and inversion.
* Visualization of optimization results and algorithm performance
* History of results arcchived in database as a list, as well as in form of PDF file

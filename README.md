# GraphQL API for Tutti Web Scraper Project

**Mini Challenge 3 - wdb @ FHNW BSc Data Science**

**Author: Lukas Reber**

GraphQL API built with Django and Graphene. The API is used by the Selenium Web Scraping Script (found [here](https://github.com/lukasreber/wdb_scraper)) to store and update data in the database.

Since this is only a proof of concept, the internal django sqlite3 database was used to store data.

## Installation

Copy repository

    git clone https://github.com/lukasreber/wdb_graphql

Create new virtual environment

    python -m venv venv

Activate virtual environment

    source venv/bin/activate

Install dependencies

    pip install -r requirements.txt

Start Django webserver

    python manage.py runserver

## Query / Documentation

The project comes with GraphiQL installed, which is a simple UI to access the API and browse the data model. It can be found here: [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)

## Testing

Run tests with

    cd tuttidata
    pytest -W ignore::DeprecationWarning

Note: there are currently some DepricationWarnings from the graphene library

### Resources

* [howtographql](https://www.howtographql.com/basics/0-introduction/)
* [docs.graphene-python](https://docs.graphene-python.org/en/latest/testing/)
* [morningpython](https://morningpython.com/2019/12/23/unit-testing-graphene-django-api-with-pytest/)

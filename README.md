# GraphQL API for Tutti Web Scraper Project

**Mini Challenge 3 - wdb @ FHNE BSc Data Science**

**Author: Lukas Reber**

GraphQL API built with Django and Graphene. The API is used by the Selenium Web Scraping Script (found [here](https://github.com/lukasreber/wdb_scraper)) to store and update data in the database.

Since this is only a proof of concecpt, the internal django sqlite3 database was used to store data.

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

The project comes with Graph*i*QL installed, which which is a simple UI to access the API. It can be accesses on the following url: [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)

## Testing

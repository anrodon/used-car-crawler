![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![License](https://img.shields.io/github/license/mashape/apistatus.svg)
# Used Car Crawler

A Python Scrapy used car crawler

## Dependencies

You have to install [Scrapy](https://github.com/scrapy/scrapy) which can be done by:

````
pip install scrapy
`````
For more details see the install section in the Scrapy documentation: http://doc.scrapy.org/en/latest/intro/install.html

You also will have to get a PostgreSQL Database where the data will be stored in.

## How to use

To start crawling [coches.net](https://www.coches.net) you only have to do 4 things:

### 1. Clone the repository

You can do that by typyng:

````
git clone https://github.com/anrodon/used-car-crawler.git
````

### 2. Create the PostgreSQL table

You need to store the bot data in a PostgreSQL table. You can do that by typing:

````
psql -U username -d database ./sql/car_table_creation.sql
````
then you are prompted to enter the password of the user, when you do that the table will be created.

### 3. Edit your DB info at cochesNet/pipelines.py

At the line:

````
db = CarDB('host', 'dbname', 'user', 'password')
````

Change the information required to let the crawler store the data in your DB.

### 4. Crawl!

Now you have just to run your crawler typing:

````
scrapy crawl coches_net
````


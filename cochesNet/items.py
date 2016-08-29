import scrapy


class Car(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    version = scrapy.Field()
    year = scrapy.Field()
    km = scrapy.Field()
    region_level2 = scrapy.Field()
    price = scrapy.Field()
    category_level1 = scrapy.Field()
    category_level2 = scrapy.Field()
    category_level3 = scrapy.Field()
    warranty = scrapy.Field()
    car_body = scrapy.Field()
    fuel = scrapy.Field()
    transmission = scrapy.Field()
    power = scrapy.Field()
    creation_date = scrapy.Field()
    color = scrapy.Field()
    num_car_doors = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()

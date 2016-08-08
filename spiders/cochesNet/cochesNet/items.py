import scrapy


class Car(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    version = scrapy.Field()
    from_year = scrapy.Field()
    km = scrapy.Field()
    from_location = scrapy.Field()
    price = scrapy.Field()

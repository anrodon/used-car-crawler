import scrapy

from cochesNet.items import Car


class CochesNetSpider(scrapy.Spider):
    name = "coches_net"
    allowed_domains = ["coches.net"]
    start_urls = [
        "http://www.coches.net/ocasion/"
    ]

    def parse(self, response):
        for href in response.xpath('//a[@class="mt-CardAd-link"]/@href').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_car)
        for href in response.xpath('//a[@class="mt-Pagination-link mt-Pagination-link--next "]/@href').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)

    def parse_car(self, response):
        car = Car()
        for js_script in response.xpath('//script[@type="text/javascript"]/text()').extract():
            if ' var' == js_script[:4]:
                for line in js_script.split(';'):
                    line = line.split('=')
                    if line[0] == ' utag_data.brand':
                        car['brand'] = line[1][1:-1]
                    if line[0] == ' utag_data.model':
                        car['model'] = line[1][1:-1]
                    if line[0] == ' utag_data.version':
                        car['version'] = line[1][1:-1]
                    if line[0] == ' utag_data.year':
                        car['year'] = line[1][1:-1]
                    if line[0] == ' utag_data.km':
                        car['km'] = line[1][1:-1]
                    if line[0] == ' utag_data.region_level2':
                        car['region_level2'] = line[1][1:-1]
                    if line[0] == ' utag_data.price':
                        car['price'] = line[1][1:-1]
                    if line[0] == ' utag_data.category_level1':
                        car['category_level1'] = line[1][1:-1]
                    if line[0] == ' utag_data.category_level2':
                        car['category_level2'] = line[1][1:-1]
                    if line[0] == ' utag_data.category_level3':
                        car['category_level3'] = line[1][1:-1]
                    if line[0] == ' utag_data.warranty':
                        car['warranty'] = line[1][1:-1]
                    if line[0] == ' utag_data.car_body':
                        car['car_body'] = line[1][1:-1]
                    if line[0] == ' utag_data.fuel':
                        car['fuel'] = line[1][1:-1]
                    if line[0] == ' utag_data.transmission':
                        car['transmission'] = line[1][1:-1]
                    if line[0] == ' utag_data.power':
                        car['power'] = line[1][1:-1]
                    if line[0] == ' utag_data.creation_date':
                        car['creation_date'] = line[1][1:-1]
                    if line[0] == ' utag_data.color':
                        car['color'] = line[1][1:-1]
                    if line[0] == ' utag_data.num_car_doors':
                        car['num_car_doors'] = line[1][1:-1]
                    if line[0] == ' utag_data.company':
                        car['company'] = line[1][1:-1]

        for description in response.xpath('//meta[@property="og:description"]/@content').extract():
            car['description'] = description

        yield car

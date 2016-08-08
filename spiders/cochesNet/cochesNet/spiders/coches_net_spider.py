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

    def parse_car(self, response):
        for js_script in response.xpath('//script[@type="text/javascript"]/text()').extract():
            if ' var' == js_script[:4]:
                car = Car()
                for line in js_script.split(';'):
                    line = line.split('=')
                    if line[0] == ' utag_data.brand':
                        car['brand'] = line[1][1:-1]
                    if line[0] == ' utag_data.model':
                        car['model'] = line[1][1:-1]
                    if line[0] == ' utag_data.version':
                        car['version'] = line[1][1:-1]
                    if line[0] == ' utag_data.year':
                        car['from_year'] = line[1][1:-1]
                    if line[0] == ' utag_data.km':
                        car['km'] = line[1][1:-1]
                    if line[0] == ' utag_data.region_level2':
                        car['from_location'] = line[1][1:-1]
                    if line[0] == ' utag_data.price':
                        car['price'] = line[1][1:-1]
                yield car

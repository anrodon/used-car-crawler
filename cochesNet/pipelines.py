import psycopg2
from storage import CarDB
from datetime import datetime
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



class CochesNetPipeline(object):
    def process_item(self, item, spider):
        db = CarDB('host', 'dbname', 'user', 'password')
        cursor = db.cursor()
        cursor.execute("INSERT INTO cars (price, brand, model, year, km, region_level2, version, category_level1, category_level2, category_level3, warranty, car_body, fuel, transmission, power, creation_date, color, num_car_doors, company, description) VALUES " +
                       "({0}, '{1}', '{2}', {3}, {4}, '{5}', '{6}', '{7}', '{8}', '{9}', {10}, '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', {17}, '{18}', '{19}')".format(
                           item['price'], item['brand'].encode('utf-8'), item['model'].encode('utf-8'), item['year'],item['km'], item['region_level2'].encode('utf-8'),
                           item['version'].encode('utf-8'), item['category_level1'].encode('utf-8'), item['category_level2'].encode('utf-8'), item['category_level3'].encode('utf-8'),
                           item['warranty'], item['car_body'].encode('utf-8'), item['fuel'].encode('utf-8'), item['transmission'].encode('utf-8'), item['power'].encode('utf-8'),
                           datetime.strptime(item['creation_date'], '%d/%m/%Y %H:%M:%S'), item['color'], item['num_car_doors'], item['company'].encode('utf-8'), item['description'].encode('utf-8')))
        db.commit();
        cursor.close();
        db.close();
        return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

# 201906140011 许泓涛
class Test1Pipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://ArdentXu:qwaszx1008612@localhost:27017/')
        self.db = self.client['spider']
        self.table = self.db['ABC']

    def process_item(self, item, spider):
        self.table.insert(dict(item))
        return item

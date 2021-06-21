# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 201906140011 许泓涛
class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()

    # 股票基本数据

    # 股票名
    BK300_name = scrapy.Field()
    # 编号
    BK300_code = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 开盘
    opening = scrapy.Field()
    # 收盘
    closing = scrapy.Field()
    # 最高
    highest = scrapy.Field()
    # 最低
    lowest = scrapy.Field()
    # 涨跌幅
    change = scrapy.Field()
    # 涨跌额
    change_amount = scrapy.Field()
    # 成交量
    vol = scrapy.Field()
    # 成交额
    turnover = scrapy.Field()
    # 振幅
    amplitude = scrapy.Field()
    # 换手率
    tun = scrapy.Field()

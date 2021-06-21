import scrapy
import re
from test1.items import Test1Item

# 201906140011 许泓涛
class WebUrlSpider(scrapy.Spider):
    name = 'web_url'
    # 可爬取的网站，可将此注释掉
    allowed_domains = ['quote.eastmoney.com']
    temp_urls = []

    for i in range(1, 16):
        # 翻页
        str3 = 'http://57.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124042387154232186663_1622701819548&pn={i}&pz=20' \
               '&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:BK0500+f:!50&fields=f1,f2,f3,f4,' \
               'f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,' \
               'f45&_=1622701819549'.format(i=i)
        temp_urls.append(str3)

    start_urls = temp_urls

    def parse(self, response):
        #   导入item
        item = Test1Item()

        #   转化成str
        decode_body = response.body.decode('utf-8').replace("'", '"')

        self.log(type(decode_body))

        #   正则表达式匹配出要转化的内容
        patten = re.compile(r'[(](.*?)[)]', re.S)
        pa_str = re.findall(patten, decode_body)

        #   取数组第0个用eval转化成字典
        dict_str = eval(pa_str[0])

        diffs = dict_str['data']['diff']

        for diff in diffs:
            item['url'] = diff['f12']
            item['BK300_name'] = diff['f14']
            yield item


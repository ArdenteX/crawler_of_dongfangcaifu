import scrapy
import json
import re
from test1.items import Test1Item

# 201906140011 许泓涛
class DongFangCaiFuSpider(scrapy.Spider):
    name = 'dongfangcaifu'
    allowed_domains = ['web']

    temp_urls = []
    filename = 'D:\\PythonX\\test1\\json_url4.json'
    with open(filename) as f:
        js = json.load(f)
        for item in js:
            temp_urls.append(item['url'])

    start_urls = temp_urls

    def parse(self, response):

        #   转化成str
        decode_body = response.body.decode('utf-8').replace("'", '"')

        #   正则表达式匹配出要转化的内容
        patten = re.compile(r'[(](.*?)[)]', re.S)
        pa_str = re.findall(patten, decode_body)

        #   取数组第0个用eval转化成字典
        dict_str = eval(pa_str[0])
        re_data_klines = dict_str['data']['klines']

        #   传入数据
        for data_item in re_data_klines:
            item = Test1Item()
            #   切割
            data_split = data_item.split(',')

            #   传入参数
            item['BK300_name'] = dict_str['data']['name']
            item['BK300_code'] = dict_str['data']['code']
            item['time'] = data_split[0]
            item['opening'] = data_split[1]
            item['closing'] = data_split[2]
            item['highest'] = data_split[3]
            item['lowest'] = data_split[4]
            item['change'] = data_split[8]
            item['change_amount'] = data_split[9]
            item['vol'] = data_split[5]
            item['turnover'] = data_split[6]
            item['amplitude'] = data_split[7]
            item['tun'] = data_split[10]

            yield item

        self.log("完成！")






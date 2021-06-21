from browsermobproxy import Server
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import time
import re
import json


def proxy():
    #   启动browsermob代理服务
    server = Server("D:\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
    server.start()
    server_proxy = server.create_proxy()

    #   配置selenium
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server={0}".format(server_proxy.proxy))
    driver = webdriver.Chrome(chrome_options=chrome_options)

    #   抓取地址
    server_proxy.new_har('ste', options={'captureHeaders': True, 'captureContent': True})

    i = 1
    urls = plus_url()
    list_urls = []

    with open('D:\\PythonX\\test1\\json_url4.json', 'w+') as f:
        for url in urls:
            #   开始
            driver.get(url)

            #   点击事件
            e_click = driver.find_element_by_xpath('//*[@id="scale-minus"]')
            e_click.click()

            result = server_proxy.har
            time.sleep(3)
            # print(result)

            final_url = ''

            for entry in result['log']['entries']:

                _url = entry['request']['url']

                match_str = re.search(r'http?://(.*?)push2his(.*?)/api/qt/stock/kline/get\S+', _url)
                if match_str is not None:
                    final_url = _url

            try:
                if i == 51:
                    break

                dict_url = {'id': i, 'url': final_url}
                list_urls.append(dict_url)
                print('已完成： ' + str(i))
                i = i + 1
                time.sleep(2)

            except NoSuchElementException:
                print(url + ": 该网页没有拉长选项")
                continue

            except WebDriverException:
                print("未知原因")
                continue

        json.dump(list_urls, f)

    print("已完成")

    server.stop()
    driver.quit()


def plus_url():
    file_name = 'D:\PythonX\\test1\\items.json'
    base_url_1 = 'http://quote.eastmoney.com/unify/r/1.'
    base_url_2 = 'http://quote.eastmoney.com/unify/r/0.'
    urls = []

    with open(file_name) as f:
        js = json.load(f)

        for item in js:

            if '6' not in item['url'][0]:
                url = base_url_2 + item['url']
                urls.append(url)
                continue

            url = base_url_1 + item['url']
            urls.append(url)

    return urls



proxy()


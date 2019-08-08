
import requests
from lxml import html

def spider(sn):
    """爬取京东的图书数据"""
    url = 'https://search.jd.com/Search?keyword={0}'.format(sn)
    #获取HTML文档
    resp  = requests.get(url, headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2601.400'
    })
    print(resp.encoding)
    resp.encoding = 'utf-8'
    html_doc = resp.text
    #获取xpath对象
    selector = html.fromstring(html_doc)
    print(len(selector))
    #找到列表的集合
    li_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print(len(li_list))
    #解析对应的内容，标题，价格，链接
    for li in li_list:
        #标题
        title = li.xpath('div/div[@class="p-name"]/a/@title')
        print(title[0])
        #购买链接
        link = li.xpath('div/div[@class="p-name"]/a/@href')
        print(link[0])
        #价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
        print(price[0])
        #店铺
        store = li.xpath('div/div[@class="p-shopnum"]/a/@title')
        #store = li.xpath('//div//a[@class="curr-shop"]/@title')
        #store = '京东自营' if len(store) == 0  else store[0]
        print(store[0])

        print('------------------')

if __name__ == '__main__':
    spider('9787115428028')
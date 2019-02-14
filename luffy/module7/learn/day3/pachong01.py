

'''

基于ajax的get请求
- 需求: 抓取豆瓣电影上的电影详情数据

import requests
url = 'https://movie.douban.com/j/chart/top_list?'

params = {
    'type': '13',
    'interval_id': '100:90',
    'action': '',
    'start': '120',
    'limit': '20',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

response = requests.get(url=url, params=params, headers=headers)

print(response.text)

'''


'''

基于ajax的post请求
    - 需求: 爬去肯德基城市餐厅位置信息


import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

# 处理post请求的参数
data = {
    'cname': '',
    'pid': '',
    'keyword': '上海',
    'pageIndex': '1',
    'pageSize': '10',
}

# 自定义请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

# 2 发起基于ajax的post请求
response = requests.post(url=url, headers=headers, data=data)
print(response.text)

'''


'''

requests 综合项目实战
    - 需求: 爬去搜狗知乎某一个词条对应的一定范围页码
import requests

url = 'https://zhihu.sogou.com/zhihu'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

word = input('enter a word:')

# 设置指定页码
start_pageNum = int(input('input start num:'))
end_pageNum = int(input('input end num:'))

for page in range(start_pageNum, end_pageNum+1):

    param = {
        'query': word,
        'page': page,
        'ie': 'utf-8'
    }

    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text

    with open(page, 'w', encoding='utf-8') as f:
        f.write(page_text)
        print('打印%d页' % page)

'''


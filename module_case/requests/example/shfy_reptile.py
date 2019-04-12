
import requests
from bs4 import BeautifulSoup
import json
import time
import datetime


def get_html(url, data):

    '''
        定义获取网页方法
    :param url:
    :param data:
    :return:
    '''

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    response = requests.get(url, params=data, headers=headers)

    return response.text

def parse_html(html):

    '''

    :param html:
    :return:
    '''

    soup = BeautifulSoup(html, 'lxml')




def get_page_nums():

    '''
    :return: 返回需要爬取的总页数
    '''

    base_url = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp?'
    # base_url = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search_content.jsp'

    data = {
        'ktrqks': '2019-04-10',
        'ktrqjs': '2019-05-10',
    }

    html = get_html(base_url, data)
    soup = BeautifulSoup(html, 'lxml')

    if soup.body.text.strip() == "系统繁忙":
        print("系统繁忙, 登录太频繁, IP被封锁")
        exit()

    res = soup.find("div", class_="meneame")
    page_nums = res.find('strong').text
    page_nums = int(page_nums)

    if page_nums % 15 == 0:
        page_nums = page_nums // 15
    else:
        page_nums = page_nums // 15 + 1

    print('总页数: ', page_nums)

    return page_nums


def main():
    '''

    循环爬取数据

    :return:
    '''

    # 获取爬取数据页数
    page_nums = get_page_nums()

    if not True:
        return

    base_url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp?"

    while True:
        page_num = 1

        data = {
            'ktrqks': '2019-04-10',
            'ktrqjs':  '2019-05-10',
            'pagesnum': page_num
        }

        while page_num <= page_nums:
            print(data)

            while True:
                html = get_html(base_url, data)
                soup = BeautifulSoup(html, 'lxml')
                if soup.body.text.strip() == '系统繁忙':
                    print('系统繁忙, IP封锁')
                    break
                else:
                    break



if __name__ == '__main__':
    main()

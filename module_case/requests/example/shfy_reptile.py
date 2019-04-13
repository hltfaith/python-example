import requests
from bs4 import BeautifulSoup
import json
import time
import datetime


'''

    项目背景
    爬取上海市高级法院普通案件传票时间

'''

def get_html(url, data):

    '''
        定义获取网页方法
    :param url:
    :param data:
    :return:
    '''
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }


        proxies = {
            'http': '203.156.209.121:8080',
            'https': '111.177.165.174:9999'
        }

        time.sleep(1)
        response = requests.get(url, params=data, headers=headers, proxies=proxies)

        # print(response.text)
        return response.text

    except requests.exceptions.ProxyError:
        print('Proxy 地址连接超时!!!')

    except requests.exceptions.ChunkedEncodingError:
        print('EncodingError')


def parse_html(html):

    '''
    :param html:  传入html源码
    :return:   通过yield生成一个生成器，存储爬取的每行信息
    '''


    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("table", attrs={"id": "report"})
    trs = table.find("tr").find_next_siblings()
    for tr in trs:
        tds = tr.find_all("td")
        yield [
            tds[0].text.strip(),
            tds[1].text.strip(),
            tds[2].text.strip(),
            tds[3].text.strip(),
            tds[4].text.strip(),
            tds[5].text.strip(),
            tds[6].text.strip(),
            tds[7].text.strip(),
            tds[8].text.strip(),
        ]



def write_to_file(content):
    '''

    要写入文件的内容

    :param content:
    :return:
    '''

    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+"\n")

def get_page_nums():

    '''
    :return: 返回需要爬取的总页数
    '''
    try:
        # base_url = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp?'
        base_url = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search_content.jsp'

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

    except AttributeError:
        print('获取总页数： NoneType !!!')
        exit()

def main():
    '''
    循环爬取数据
    :return:
    '''

    # 获取爬取数据页数
    page_nums = get_page_nums()
    time.sleep(1)


    if not True:
        return

    # base_url = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp?'
    # base_url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp?"
    base_url = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search_content.jsp'

    while True:
        page_num = 1

        data = {
            'ktrqks': '2019-04-10',
            'ktrqjs':  '2019-05-10',
            'pagesnum': page_num
        }

        while page_num <= page_nums:

            # while True:
            #     html = get_html(base_url, data)
            #     soup = BeautifulSoup(html, 'lxml')
            #     if soup.body.text.strip() == '系统繁忙':
            #         print('系统繁忙, IP封锁')
            #         break
            #     else:
            #         break
            time.sleep(1)

            html = get_html(base_url, data)
            res = parse_html(html)


            for i in res:
                write_to_file(i)

            print('爬取完第[%s]页, 总共[%s]页' % (page_num, page_nums))
            page_num += 1
            data["pagesnum"] = page_num

        else:
            print('爬取完毕')
            break

if __name__ == '__main__':
    main()

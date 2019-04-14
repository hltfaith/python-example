import requests

'''
这里通过伯乐在线为例子，这个相对于第一种就比较简单了，没有太多的分析过程直接发送post请求，然后获取cookie,通过cookie去访问其他页面,下面直接是代码实现例子：
http://www.jobbole.com/bookmark/ 这个地址是只有登录之后才能访问的页面，否则会直接返回登录页面
'''

def login():
    url = "http://www.jobbole.com/wp-admin/admin-ajax.php"
    data = {
        "action": "user_login",
        "user_login":"zhaofan1015",
        "user_pass": '******',
    }
    response = requests.post(url,data)
    cookie = response.cookies.get_dict()
    print(cookie)
    url2 ="http://www.jobbole.com/bookmark/"
    response2 = requests.get(url2,cookies=cookie)
    print(response2.text)

login() 


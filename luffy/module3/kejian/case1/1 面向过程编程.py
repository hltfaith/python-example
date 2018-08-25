'''
面向过程：核心是过程二字，过程指的是解决问题的步骤，设计一条流水线，机械式的思维方式
优点：复杂的问题流程化，进而简单化
缺点：可扩展性差
'''

import json
import re
def interactive():
    name=input('>>: ').strip()
    pwd=input('>>: ').strip()
    email=input('>> ').strip()
    return {
        'name':name,
        'pwd':pwd,
        'email':email
    }

def check(user_info):
    is_valid=True

    if len(user_info['name']) == 0:
        print('用户名不能为空')
        is_valid=False

    if len(user_info['pwd']) < 6:
        print('密码不能少于6位')
        is_valid=False

    if not re.search(r'@.*?\.com$',user_info['email']):
        print('邮箱格式不合法')
        is_valid=False

    return {
        'is_valid':is_valid,
        'user_info':user_info
    }

def register(check_info):
    if check_info['is_valid']:
        with open('db.json','w',encoding='utf-8') as f:
            json.dump(check_info['user_info'],f)



def main():
    user_info=interactive()

    check_info=check(user_info)

    register(check_info)

if __name__ == '__main__':
    main()
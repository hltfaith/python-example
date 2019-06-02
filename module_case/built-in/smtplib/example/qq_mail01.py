#coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

'''
使用qq的邮件服务器需要注意的两个地方主要是：

1.协议问题 使用465端口 SSL 协议

2.口令问题 出现SMTPAuthenticationError 主要的原因就是口令和帐号信息不对，这里我们使用qq服务器发送 需要先到邮箱里设置独立密码(必须), 然后开启

   SMTP/POP3服务。然后用qq手机安全中心扫一扫会给一个授权码, 在代码中要填写的密码是这个授权码， 而不是邮箱密码！
'''

mail_info = {
    "from": "xxxx@qq.com",
    "to": "xxx@qq.com",
    "hostname": "smtp.qq.com",
    "username": "xxx@qq.com",
    "password": "xxx",
    "mail_subject": "test",
    "mail_text": "hello, this is a test email, sended by py",
    "mail_encoding": "utf-8"
}

if __name__ == '__main__':
    #这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)
    
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])

    msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

    smtp.quit()



# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import smtplib
from email.message import EmailMessage

# 定义SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 定义发件人地址
from_addr = '1012047386@qq.com'
# 定义登录邮箱的密码
password = 'xxawgltltzlebbba'
# 定义收件人地址:
to_addr = 'eric_wangyz@foxmail.com'

# 创建SMTP连接
#conn = smtplib.SMTP(smtp_server, 25)
conn = smtplib.SMTP_SSL(smtp_server,465)
conn.set_debuglevel(1)
conn.login(from_addr, password)            #①
# 创建邮件对象
msg = EmailMessage()
# 设置邮件内容
msg.set_content('您好，这是一封来自Python的邮件', 'plain', 'utf-8')
msg['subject'] = '一封来自Python的邮件'
msg['from'] = '%s' % from_addr
msg['to'] = '%s' % to_addr
# 发送邮件
conn.sendmail(from_addr, [to_addr], msg.as_string())
# 退出连接
conn.quit()
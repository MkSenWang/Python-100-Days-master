# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import re

# 需求1：匹配从0到100的数字,包括100
print(re.match('[1-9]?\d','98').group())
# print(re.match('[1-9]?\d$','100').group())
print(re.match('[1-9]?\d$|100','100').group())

# 需求2:匹配网易邮箱,163.com也可以是126.com
emails = '''
  awhahlf@163.com
affafafafaaaaaaaaaaaaaaaa@163.com
afa_@163.com
225afafaf@163.com
aaaa____@126.com
aaaa____@163.com
'''
print(re.search('^[a-zA-Z][\w]{5,17}@(163|126)\.com$',emails,re.MULTILINE).group())

# 需求3： 匹配<标签>xxxx</标签>

print(re.match('<[a-zA-Z]+>\w*</[a-zA-Z]+>','<div>hello</div>'))
print(re.match('<[a-zA-Z]+>\w*</[a-zA-Z]+>','<p>hello</p>'))
# print(re.match('<[a-zA-Z]+>\w*</[a-zA-Z]+>','<p>hello</div>')) # 非法
print(re.match(r'<([a-zA-Z]+)>\w*</\1>','<p>hello</p>')) # 非法

# 第二种写法,匹配一个网页的嵌套标签
# line = '<div><p> hello </p></div>'
line = '<div><p> hello </h2></div>'

print(re.match(r'<(?P<n1>\w*)><(?P<n2>\w*)>.*</(?P=n2)></(?P=n1)>',line).group())

# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import re

emails = '''
awhahlf@163.com
affafafafaaaaaaaaaaaaaaaa@163.com
afa_@163.com
225afafaf@163.com
aaaa____@126.com
aaaa____@163.com
'''
list = re.findall('(^[a-zA-Z][\w]{5,17}@(163|126)\.com$)',emails,re.MULTILINE)
for email in list:
    print(email[0])


# 需求，匹配一个数字，把匹配结果的数字加1返回
def add(result): # result是一个匹配对象
    str_number = result.group()
    num = int(str_number) +1
    return str(num)

print(re.sub(r'\d+',add,'python = 188'))

line = "hello, world, beijing."

print(re.split(r'\W+',line))

print(re.split(r':| ','info:xiaoZhang 33 shandong'))


line2 = 'This is my tel:188-9999-8888'
# 非贪婪模式，需求：把电话和电话的描述信息尽可能的分开，只能用正则表达式
result = re.match(r'(.+?)(\d+-\d+-\d+)',line2)
print(result.group(1))
print(result.group(2))
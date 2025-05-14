# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import re
# 练习5： 匹配163的邮箱地址，用户名包含6~18个字符，可以是字母，数字，下划线，但是必须以字母开头
emails = '''
  awhahlf@163.com
affafafafaaaaaaaaaaaaaaaa@163.com
afa_@163.com
225afafaf@163.com
aaaa____@126.com
aaaa____@163.comabc
bbb____@163.com
'''
print(re.search('^[a-zA-Z][\w]{5,17}@163\.com',emails,re.MULTILINE).group())

#取反
print(re.search('[^0-9]','1234'))
print(re.search('^[0-9]','1234'))

print(re.search('^[a-zA-Z][\w]{5,17}@163\.com$',emails,re.MULTILINE).group())


print(re.search(r'.*\bchangsha\b','I love changsha too'))
print(re.search(r'.*\bchangsha\b','I love changshanan too'))
# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import re

# 需求1：匹配一个字符串第一个字母是大写，后面的字母必须是小写或者没有

print(re.match('[A-Z][a-z]*','Mm').group())
print(re.match('[A-Z][a-z]*','M').group())
print(re.match('[A-Z][a-z]*','Mabcdfds').group())

# 需求2：匹配一个变量名
print(re.match(r'[a-zA-Z_]+[\w]*','name1'))
print(re.match(r'[a-zA-Z_]+[\w]*','_name1'))
print(re.match(r'[a-zA-Z_]+[\w]*','2_name1'))

# 需求3：匹配从0到99之间的任意一个数子
print(re.match('[0-9]?[0-9]','77'))
print(re.match('[0-9]?[0-9]','7'))
print(re.match('[0-9]?[0-9]','09'))
print(re.match('[0-9]?[0-9]','999'))

# 需求4：匹配密码（8-20位，可以是大小写的字母，数字，下划线）
print(re.match('[a-zA-Z0-9_]{8,20}','12345678').group())
print(re.match('[a-zA-Z0-9_]{6}','123456').group())

# 练习5： 匹配163的邮箱地址，用户名包含6~18个字符，可以是字母，数字，下划线，但是必须以字母开头
emails = '''
awhahlf@163.com
affafafafaaaaaaaaaaaaaaaa@163.com
afa_@163.com
225afafaf@163.com
aaaa____@qq.com
aaaa____@163.com
'''

print(re.search('[a-zA-Z][\w]{5,17}@163\.com',emails).group())


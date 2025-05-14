# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import re

one = 'a'
print(re.match('.',one).group())

two = '2'
two_2 = 'hello Python'
print(re.match('[1,2,3]',two).group())
print(re.match('[hH]',two_2).group()) # 匹配大小或者小写的H

three= '天空8号发射成功'

print(re.match('天空\d',three).group())
print(re.search('\d',three).group())
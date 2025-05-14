# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
path = 'C:\\a\\b\\c' # 文件路径

print(path)
import re

print(re.match('C:\\\\',path).group())

# 字符串前面使用r,代表python中的原生字符串
print(re.match(r'C:\\',path).group())
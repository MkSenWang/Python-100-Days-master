# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌
import re

tel_l = '''
aesdf
13811011234
aa1a3hi233rhi3
87156340
affa124564531346546
afa19454132135
'''

tel_2 = "13812345678abc"

pattern = re.compile(r'1[3,9]\d{9}') # 编译正则表达式之后得到一个编译对象

result = pattern.search(tel_l) # search 只会返回第一个匹配的结果，如果没有匹配成功则返回None
print(result)
print(result.group()) # 返回第一个匹配结果
print(result.span()) # 返回第一个匹配结果的下标




result2 = pattern.match(tel_2) # match 函数是从第一个字符开始匹配，如果第一个字符不匹配，返回None
print(result2.group(0))
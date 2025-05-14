#教育机构 ：马士兵教育
#讲    师：杨淑娟
s='天涯共此时'
#编码
print(s.encode(encoding='GBK'))  #在GBK这种编码格中 一个中文占两个字节
print(s.encode(encoding='UTF-8')) #在UTF-8这种编辑格式中，一个中文占三个字节

#解码
#byte代表就是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK')   #编码
print(byte.decode(encoding='GBK')) #解码

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))






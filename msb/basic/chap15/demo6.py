#教育机构 ：马士兵教育
#讲    师：杨淑娟

src_file=open('logo.png','rb')

target_file=open('copylogo.png','wb')

target_file.write(src_file.read())

target_file.close()
src_file.close()


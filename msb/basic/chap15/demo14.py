#教育机构 ：马士兵教育
#讲    师：杨淑娟
with open('logo.png','rb') as src_file:
    with open('copy2logo.png','wb') as target_file:
        target_file.write(src_file.read())

#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  os
path=os.getcwd()
lst_files=os.walk(path)
for dirpath,dirname,filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('-------------------------------------')'''
    for dir in dirname:
        print(os.path.join(dirpath,dir))

    for file in filename:
        print(os.path.join(dirpath,file))
    print('----------------------------------')
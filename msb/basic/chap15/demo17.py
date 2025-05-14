#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  os.path
print(os.path.abspath('demo13.py'))
print(os.path.exists('demo13.py'),os.path.exists('demo18.py'))
print(os.path.join('E:\\Python','demo13.py'))
print(os.path.split('E:\\vipython\\chap15\\demo13.py'))
print(os.path.splitext('demo13.py'))
print(os.path.basename('E:\\vippython\\chap15\\demo13.py'))
print(os.path.dirname('E:\\vippython\\chap15\\demo13.py'))
print(os.path.isdir('E:\\vippython\\chap15\\demo13.py'))
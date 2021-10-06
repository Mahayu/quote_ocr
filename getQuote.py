import json
from PIL import Image
from types import SimpleNamespace


#  json->dicts->objs
class pic:
    def __init__(self,id,path,info,keyWord):
       self.id = id
       self.path = path
       self.info = info
       self.keyWord = keyWord


pics = []
with open('data\picData.json',mode='r',encoding='UTF-8') as f:
    picsDict = json.load(f)
#  字典转obj
for singlePicDict in picsDict:
    singlePic = pic(0,"","","")
    singlePic = SimpleNamespace(**singlePicDict)
    pics.append(singlePic)


print("测试用语录提取程序")
print("读取语录关键词。")
for pic in pics:
    print(str(pic.id) + " " + str(pic.keyWord))
while(True):
       print("输入关键词对应的id展示图片")
       inputId = input()
       for pic in pics:
          if str(pic.id) == inputId:
              try:
                    img = Image.open(pic.path)
                    img.show()
              except:
                    print("没找到语录图片，请重新生成json。")
       print("不错，很有精神。要再来吗？不用的话直接关掉就好。")
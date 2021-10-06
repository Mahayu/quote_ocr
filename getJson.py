import os
import json
import jieba.analyse
from paddleocr import PaddleOCR

#  总之就是先用类标识，后面存json再用字典
#  也就是objs->dicts->json.
class pic:
    def __init__(self,id,path,info,keyWord):
       self.id = id
       self.path = path
       self.info = info
       self.keyWord = keyWord

#  多字典组成的list->json
def pic2json(pics):
    with open("data\picData.json",'w',encoding="UTF-8") as f:
        json.dump(pics,f,indent=4,sort_keys=True)


picFolder = "imgs//"
allPicPath = os.listdir(picFolder)
ocr = PaddleOCR(
    enable_mkldnn=True,
    use_gpu=False,
    lang="ch"
)
pics = []
badPicPath = []
givenId = 1

try:
    os.remove(picFolder + "put_imgs_here")
except: OSError

for paths in allPicPath:
    paths = 'imgs/' + paths
    result = ocr.ocr(paths, cls=True)
    for line in result:
        lastQuote = line[-1]  #  多行文本的情况下默认选最后一行
    try:
        singlePic = pic(0,"","","")
        singlePic.id = givenId
        givenId += 1
        singlePic.info = lastQuote[0]
        singlePic.path = paths
        if(len(singlePic.info) >= 7):  #  多关键词，多行文本以后再改良
            singlePic.keyWord = jieba.analyse.extract_tags(
            singlePic.info, topK=4, withWeight=False, allowPOS=()
            )  # 使用嵌套字典。顺带一提"恶劣影响"分词会变成"劣影"。。。”
        else:
            singlePic.keyWord = lastQuote[0]
        pics.append(singlePic.__dict__)  #  Class->Dict->List，便于输出json
    except IndexError:
        badPicPath.append(paths)
        next

pic2json(pics)
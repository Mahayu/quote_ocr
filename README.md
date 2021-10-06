
# 一个群语录提取脚本

大概就是一个群语录提取脚本，利用Paddleocr实现。

## 使用

首先往/imgs里面导入你所需要的语录文件，要求见下。

运行`pip install -r requirements.txt`来安装对应的包，注意在Windows10环境下需要安装MSVC。

运行getJson.py获得picData.json，然后运行getQuote.py即可。


##  文件结构

- /imgs

用于存放你要的语录图片。最好是单条语录，包含群名等不必要信息会导致未预料行为。

- /getJson.py

用于产生一个id-图片路径-关键词对应的 Json 文件以备使用。运用了 PaddleOCR 与 Jieba 作必要的工作。

- /getQuote.py

查询语录用脚本，基于id和关键词选择。

- /picData.json

存放语录-图片对应的Json文件。


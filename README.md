
# 一个群语录提取脚本

大概就是一个群语录提取脚本，利用Paddleocr实现。

## 使用

首先往/imgs里面导入你所需要的语录文件。

终端内运行`pip install -r requirements.txt`来安装对应的包，注意在Windows10环境下需要安装MSVC编译器。

默认采用CPU运算，涉及到CUDA的场合请自行处理。

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


##  QA

-  安装包时出现 `error: Microsoft Visual C++ xx.0 is required.`
   
   请安装MSVC编译器。

-  多条消息记录是如何识别的？

   考虑到兼容性（可能会将昵称文本也进行识别），默认是把最后一条文本读入标识信息当中。涉及到多条消息记录的场合，标识信息应当是最后一条的内容。

- 如果有现成的图片与json文件（不需要训练），如何更便捷的分发？

  单纯的 getQuote.py 仅需要Pillow库即可运行，分发时只需安装这个就行了。另外要注意定位到工作目录以防出现相对路径的问题。

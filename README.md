# Bert-use
简单使用bert 进行实体识别

公司里要求做一个实体识别的功能。而bert 作为现在风头最火的NLP模型 ，自然而然就想到它的强大之处。

## bert的优点
bert 优点我就不一一介绍了，获得了很多奖，同学们可以自行百度。
对于我这种菜鸟来说，其功能强大的地方在于bert做了大量的预训练，方便我们使用，对一些没有大量数据支持的人来说是个福音。它的词向量是无监督的，所以不需要大量
数据来在做预训练。

## bert使用
因为bert作为google 开发的项目，对中文支持并不是特别友好，所以我调用了 Macanv 同学的使用谷歌的BERT模型在BLSTM-CRF模型上进行预训练用于中文命名实体识别的
Tensorflow
- github 链接 https://github.com/macanv/BERT-BiLSTM-CRF-NER 
- 中文文档请查看 https://blog.csdn.net/macanv/article/details/85684284 

bert 实体识别的训练语料还是很消费人力，物力的，无论是train,test,dev 都需要把语料变成如下图所示
![image](https://github.com/ragnarokzrz/Bert-use/blob/master/%E9%A2%84%E8%AE%AD%E8%AF%AD%E6%96%99.jpg)

然后就可以调用bert 的服务了.



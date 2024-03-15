# 创建 Person 类的实例
from EmbeddingMode import ZGEmbedding

data_list = ["样例数据-3", "样例数据-4"]
emb = ZGEmbedding("为这个句子生成表示以用于检索相关文章：")
result = emb.get_embedding_array(data_list)
print(result)

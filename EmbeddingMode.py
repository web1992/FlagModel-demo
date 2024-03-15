from FlagEmbedding import FlagModel


class ZGEmbedding:
    # 类的构造函数
    def __init__(self, query_instruction):
        self.query_instruction = query_instruction

    # 类的方法
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def get_embedding_array(self, arr: list):
        model = FlagModel('D:\\Dev\\Github\\bge-small-zh-v1.5',
                          query_instruction_for_retrieval=self.query_instruction,
                          use_fp16=True)  # Setting use_fp16 to True speeds up computation with a slight performance degradation
        embeddings_1 = model.encode(arr)
        return embeddings_1


# 创建 Person 类的实例
data_list = ["样例数据-3", "样例数据-4"]
emb = ZGEmbedding("为这个句子生成表示以用于检索相关文章：")
result = emb.get_embedding_array(data_list)
print(result)

from FlagEmbedding import FlagModel


class ZGEmbedding:
    # 类的构造函数
    def __init__(self, query_instruction):
        self.query_instruction = query_instruction

    def get_embedding_array(self, arr: list):
        model = FlagModel('D:\\Dev\\Github\\bge-small-zh-v1.5',
                          query_instruction_for_retrieval=self.query_instruction,
                          use_fp16=True)  # Setting use_fp16 to True speeds up computation with a slight performance degradation
        embeddings = model.encode(arr)
        return embeddings

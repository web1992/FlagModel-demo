from store_client import StoreClient
import numpy as np
from embeddings import ZGEmbedding

store_client = StoreClient("Test4")

data_list = ["样例数据-3", "样例数据-4"]
emb = ZGEmbedding("为这个句子生成表示以用于检索相关文章：")
embeddings_docs = emb.get_embedding_array(data_list)
print(embeddings_docs)

# print('data', data)
index = list(range(len(embeddings_docs)))

v_size = len(embeddings_docs.tolist()[0])

print('v_size=', v_size)
payload = []
for i in range(len(data_list)):
    payload.append(
        {
            "doc": data_list[i]
        }
    )
store_client.get_store().upsert(index, v_size, embeddings_docs.tolist(), payload)

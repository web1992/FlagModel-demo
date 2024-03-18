from StoreClient import StoreClient
from embeddings import ZGEmbedding

# store_client = StoreClient("Test4")
store_client = StoreClient("Test-Long-text")

data_list = ["网络"]
emb = ZGEmbedding("为这个句子生成表示以用于检索相关文章：")
embeddings_docs = emb.get_embedding_array(data_list)
# print(embeddings_docs)

rs = store_client.get_store().search(embeddings_docs.tolist()[0], 10)
print('rs=', rs)


data_list = ["特斯拉汽车"]
emb = ZGEmbedding("为这个句子生成表示以用于检索相关文章：")
embeddings_docs = emb.get_embedding_array(data_list)
# print(embeddings_docs)
rs = store_client.get_store().search(embeddings_docs.tolist()[0], 10)

print('rs=', rs)

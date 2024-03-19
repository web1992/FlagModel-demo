from store_client import StoreClient
from embeddings import ZGEmbedding

store_client = StoreClient("Test-Long-md")

data_list = ["常用的GC算法"]
emb = ZGEmbedding("为这个句子生成表示以用于检索相关文章：")
embeddings_docs = emb.get_embedding_array(data_list)
# print(embeddings_docs)

rs = store_client.get_store().search(embeddings_docs.tolist()[0], 10)
# print('rs=', rs)
for r in rs:
    print(r)
    # print(r.payload['doc'])
    print("-" * 100)



from qdrant_client import QdrantClient
from qdrant_client.http import models

from store import Store


class QdrantStore(Store):
    def __init__(self, collection_name: str):
        self.client = init()
        self.collection_name = collection_name

    def upsert(self, index: list, data_list: list):
        collections = self.client.get_collections()
        print('len collections',len(list(collections)))
        if self.collection_name not in collections:
            self.client.recreate_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=100, distance=models.Distance.COSINE)
            )
        upsert_rs = self.client.upsert(
            collection_name=self.collection_name,
            points=models.Batch(
                ids=index,
                vectors=data_list
            )
        )
        print('upsert_rs', upsert_rs)

    def count(self):
        count = self.client.count(
            collection_name=self.collection_name,
            exact=True,
        )
        return count

    def search(self, query_data: list, limit: int):
        search_rs = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_data,
            limit=limit
        )
        return search_rs


def init():
    client = QdrantClient(host="124.223.35.219", port=6333)
    print('client init', client)
    return client

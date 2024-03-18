from qdrant import QdrantStore


class StoreClient:
    def __init__(self, store_name: str):
        self.store = QdrantStore(store_name)

    def get_store(self):
        return self.store

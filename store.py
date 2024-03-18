from abc import ABC, abstractmethod


class Store(ABC):
    @abstractmethod
    def upsert(self, index: list, vector_size: int, data_list: list, payload: []):
        pass

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def search(self, query_data: list, limit: int):
        pass

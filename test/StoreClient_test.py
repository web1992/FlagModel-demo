from StoreClient import StoreClient
import numpy as np

store_client = StoreClient("Test2")

data = np.random.uniform(low=-1.0, high=1.0, size=(1_000, 100))
# print('data', data)
index = list(range(len(data)))

store_client.get_store().upsert(index, data.tolist())

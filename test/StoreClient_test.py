from StoreClient import StoreClient
import numpy as np

store_client = StoreClient("Test2")

v_size = 100
data = np.random.uniform(low=-1.0, high=1.0, size=(1_000, v_size))
print('data', data)
index = list(range(len(data)))

store_client.get_store().upsert(index, v_size, data.tolist())

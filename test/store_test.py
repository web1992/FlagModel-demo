import numpy as np
from faker import Faker
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import CollectionStatus

# https://colab.research.google.com/github/qdrant/examples/blob/master/qdrant_101_getting_started/getting_started.ipynb

client = QdrantClient(host="124.223.35.219", port=6333)
print(client)

my_collection = "first_collection"

first_collection = client.recreate_collection(
    collection_name=my_collection,
    vectors_config=models.VectorParams(size=100, distance=models.Distance.COSINE)
)
print(first_collection)

collection_info = client.get_collection(collection_name=my_collection)
print(list(collection_info))
print(collection_info.points_count)

data = np.random.uniform(low=-1.0, high=1.0, size=(1_000, 100))
type(data[0, 0]), data[:2, :20]

print(data[0, 0])

index = list(range(len(data)))
print(index[-10:])

client.upsert(
    collection_name=my_collection,
    points=models.Batch(
        ids=index,
        vectors=data.tolist()
    )
)

rs_list = client.retrieve(
    collection_name=my_collection,
    ids=[100],
    with_vectors=True  # the default is False
)

print(rs_list)


def create_song():
    return np.random.uniform(low=-1.0, high=1.0, size=100).tolist()


client.upsert(
    collection_name=my_collection,
    points=[
        models.PointStruct(
            id=1000,
            vector=create_song(),
        )
    ]
)

# this will show the amount of vectors BEFORE deleting the one we just created
count = client.count(
    collection_name=my_collection,
    exact=True,
)

print(count)

# client.delete(
#     collection_name=my_collection,
#     points_selector=models.PointIdsList(
#         points=[1000],
#     ),
# )

count = client.count(
    collection_name=my_collection,
    exact=True,
)
print(count)

fake_something = Faker()
print(fake_something.name())

# payload = []
#
# for i in range(len(data)):
#     payload.append(
#         {
#             "artist": fake_something.name(),
#             "song": " ".join(fake_something.words()),
#             "url_song": fake_something.url(),
#             "year": fake_something.year(),
#             "country": fake_something.country()
#         }
#     )
#
# print(payload[:3])
#
# client.upsert(
#     collection_name=my_collection,
#     points=models.Batch(
#         ids=index,
#         vectors=data.tolist(),
#         payloads=payload
#     )
# )


# 查询
resutls = client.retrieve(
    collection_name=my_collection,
    ids=[1,10, 50, 100, 500],
    with_vectors=False,
    with_payload=True
)

print(type(resutls))
print(resutls)
print(resutls[0].payload)
print(resutls[0].id)


living_la_vida_loca = create_song()

search_rs = client.search(
    collection_name=my_collection,
    query_vector=living_la_vida_loca,
    limit=3
)

print(type(search_rs))
print(search_rs)

# Filter
aussie_songs = models.Filter(
    must=[models.FieldCondition(key="country", match=models.MatchValue(value="Australia"))]
)
type(aussie_songs)

search_rs = client.search(
    collection_name=my_collection,
    query_vector=living_la_vida_loca,
    query_filter=aussie_songs,
    limit=2
)

print(search_rs)


client.search(
    collection_name=my_collection,
    query_vector=living_la_vida_loca,
    query_filter=aussie_songs,
    with_payload=models.PayloadSelectorExclude(exclude=["year"]),
    limit=5
)


client.clear_payload(
    collection_name=my_collection,
    points_selector=models.PointIdsList(
        points=index,
    )
)

print('recommend_rs')
recommend_rs = client.recommend(
    collection_name=my_collection,
    positive=[17],
    limit=5
)
print(recommend_rs)


client.recommend(
    collection_name=my_collection,
    query_vector=living_la_vida_loca,
    positive=[17],
    negative=[120],
    limit=5
)
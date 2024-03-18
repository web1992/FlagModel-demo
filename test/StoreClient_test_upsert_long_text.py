from StoreClient import StoreClient
import numpy as np
from embeddings import ZGEmbedding

store_client = StoreClient("Test-Long-text")

data_list = [
    "把工程实践中遇到的问题，从问题类型和解法类型两个角度去归类，总结出一些有限适用的原则，就从点到了面。把诸多总结出的原则，组合应用到自己的项目代码中，就是把多个面结合起来构建了一套立体的最佳实践的方案。当你这套方案能适应 30w+行代码的项目，超过 30 人的项目，你就入门架构师了！当你这个项目是多端、多语言，代码量超过 300w 行，参与人数超过 300 人，代码质量依然很高，代码依然在高效地自我迭代，每天消除掉过时的代码，填充高质量的替换旧代码和新生的代码。恭喜你，你已经是一个很高级的架构师了！再进一步，你对某个业务模型有独到或者全面的理解，构建了一套行业第一的解决方案，结合刚才高质量实现的能力，实现了这么一个项目，恭喜你，你已经成为专家工程师了！",
    "强烈建议阅读的书籍，此书是针对计算机网络中所有使用的网络协议说明(简介+设计)的入门书籍，绝对的经典。 这些协议对我们日常开发虽然无感知，但是确实是基础设施不可缺少。但是本书涉及很多网络协议，第一次阅读会感觉吃力(至少对我来说是的 🐶)，建议多读几遍。如果有网络开发经验，阅读此书会很流畅。如果没有网络开发经验，推荐可以去阅读一些中间件中的对网络的处理，如 Dubbo,RockeMQ 中对网络部分编码，解码的处理。如果读懂了，再来读本书，会容易很多。本书中的配图很多，大部门都是关于网络协议设计的图。如果真正的理解了网络中的编码，解码操作。 那么对下面的图一定是能看懂的(或者说如果你读懂了书中的大部门内容，那么理解下图，不成问题)。"]
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

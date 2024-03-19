from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
import os

from embeddings import ZGEmbedding
from store_client import StoreClient


def read_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    return content


# 指定文件路径
file_path = "D:\\Dev\\Github\\Python-project\\demo\\demo\\md\\chapter-01.md"


# 读取文件内容
# file_content = read_file(file_path)
# print(file_content)


def read_markdown_files(directory):
    markdown_contents = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    markdown_contents.append((file_path, str(content)))
    return markdown_contents


# 指定文件夹路径
directory_path = "D:\\Dev\\Github\\Python-project\\demo\\demo\\md\\"

# 读取Markdown文件内容
markdown_files_content = read_markdown_files(directory_path)

# print(markdown_files_content)
# 打印文件路径及内容
# for file_path, content in markdown_files_content:
#     print("File:", file_path)
#     print("Content:", content)
#     print("-" * 50)


md_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=512, chunk_overlap=128
)

data_list=[]
for item in markdown_files_content:
    # print(str(item[1]))
    md_docs = md_splitter.create_documents([str(item[1])])
    # print(len(md_docs))
    for doc in md_docs:
        data_list.append(doc.page_content)
        print(doc.page_content)



store_client = StoreClient("Test-Long-md")
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


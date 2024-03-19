from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

markdown_text = """
# 🦜️🔗 LangChain

⚡ Building applications with LLMs through composability ⚡

## Quick Install

```bash
# Hopefully this code block isn't split
pip install langchain
```

As an open-source project in a rapidly developing field, we are extremely open to contributions.
"""


md_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=64, chunk_overlap=20
)
md_docs = md_splitter.create_documents([markdown_text])
print(len(md_docs))
for doc in md_docs:
    print(doc)
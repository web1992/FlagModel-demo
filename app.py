from flask import Flask, request, jsonify

from EmbeddingMode import ZGEmbedding


class App:
    def __init__(self):
        # 创建一个Flask应用
        self.app = Flask(__name__)
        # 初始化模型
        self.embedding = init_mode()

        # 定义路由和视图函数
        @self.app.route('/')
        def hello():
            return 'server started !'

        @self.app.route('/embedding')
        def embedding():
            doc = request.args.get('doc', '')
            print('doc=', doc)
            return self.do_emb([doc])

        @self.app.route('/embeddingBtch', methods=['POST'])
        def submit_form():
            if request.method == 'POST':
                # 获取 POST 请求中的原始数据
                body_content = request.get_data()
                # 可以根据需要对原始数据进行进一步处理
                # 这里只是简单地返回接收到的数据
                json_data = request.get_json()
                # 将 JSON 数据解析为类对象
                doc_body = DocBody(json_data['ext'], json_data['docs'])
                return self.do_emb(doc_body.docs)
            else:
                return 'Method Not Allowed'

    def do_emb(self, docs):
        if len(docs) == 0:
            embeddings_json = {
                'embeddingsList': []
            }
            # 返回JSON格式的embeddings_1
            return jsonify(embeddings_json)
        else:
            embeddings_rs = self.embedding.getEmbeddingArray(docs)
            embeddings_json = {
                'embeddingsList': embeddings_rs.tolist()
            }
            # 返回JSON格式的embeddings_1
            return jsonify(embeddings_json)

    def run(self):
        # 启动Flask应用，监听在本地的5000端口
        self.app.run(debug=True)


def init_mode():
    embedding = ZGEmbedding('为这个句子生成表示以用于检索相关文章')
    return embedding


class DocBody:
    def __init__(self, ext, docs: list):
        self.ext = []
        self.docs = docs


if __name__ == '__main__':
    # 创建并运行Flask应用
    my_app = App()
    my_app.run()

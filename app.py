from flask import Flask, request, jsonify

from EmbeddingMode import ZGEmbedding


class App:
    def __init__(self):
        # 创建一个Flask应用
        self.app = Flask(__name__)
        self.embedding = initMode()

        # 定义路由和视图函数
        @self.app.route('/')
        def hello():
            return 'Hello, World!'

        @self.app.route('/embedding')
        def embedding():
            doc = request.args.get('doc', '')
            print('doc=', doc)
            if len(doc) == 0:
                embeddings_json = {
                    'embeddingsList': []
                }
                # 返回JSON格式的embeddings_1
                return jsonify(embeddings_json)
            else:
                embeddings_rs = self.embedding.getEmbeddingArray([doc])
                embeddings_json = {
                    'embeddingsList': embeddings_rs.tolist()
                }
                # 返回JSON格式的embeddings_1
                return jsonify(embeddings_json)

    def run(self):
        # 启动Flask应用，监听在本地的5000端口
        self.app.run(debug=True)


def initMode():
    embedding = ZGEmbedding('为这个句子生成表示以用于检索相关文章')
    return embedding


if __name__ == '__main__':
    # 创建并运行Flask应用
    my_app = App()
    my_app.run()

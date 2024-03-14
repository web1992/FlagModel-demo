
from flask import Flask

# 创建一个Flask应用
app = Flask(__name__)

# 定义路由和视图函数
@app.route('/')
def hello():
    return 'Hello, World!'

# 如果直接运行这个文件，则启动Flask服务器
if __name__ == '__main__':
    # 启动Flask应用，监听在本地的5000端口
    app.run(debug=True)

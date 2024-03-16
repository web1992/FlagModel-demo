from FlagEmbedding import FlagModel
import sys


class ZGEmbedding:
    # 类的构造函数
    def __init__(self, query_instruction):
        self.query_instruction = query_instruction
        self.model = self._init_mode()

    def _init_mode(self):
        embedding_path = get_embedding_path()
        print('embedding_path is ', embedding_path)
        print('query_instruction is ', self.query_instruction)
        # use_fp16 = True
        # Setting use_fp16 to True speeds up computation with a slight performance degradation
        model = FlagModel(embedding_path,
                          query_instruction_for_retrieval=self.query_instruction,
                          use_fp16=True)
        return model

    def get_embedding_array(self, arr: list):
        embeddings = self.model.encode(arr)
        return embeddings


def get_embedding_path():
    embedding_path = ''
    if is_mac_os():
        embedding_path = '/Users/manfen/Documents/DEV/GITHUB/bge-small-zh-v1.5'
    elif is_window_os():
        embedding_path = 'D:\\Dev\\Github\\bge-small-zh-v1.5'
    else:
        return embedding_path
    return embedding_path


def get_platform():
    if sys.platform.startswith('win'):
        return 'Windows'
    elif sys.platform.startswith('darwin'):
        return 'macOS'
    elif sys.platform.startswith('linux'):
        return 'Linux'
    else:
        return 'Unknown'


def is_mac_os():
    return 'macOS' == get_platform()


def is_window_os():
    return 'Windows' == get_platform()

class BaseException(Exception):
    def __init__(self,msg,code):
        self.code = code
        self.msg = msg

class MoodAnalysisException(BaseException):
    pass


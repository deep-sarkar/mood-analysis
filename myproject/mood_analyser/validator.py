from . exceptions import MoodAnalysisException
from . status import response

def empty_message_raise_MoodAnalysisException(message):
    if len(message) == 0:
        raise MoodAnalysisException(code=100,msg=response[100])

def if_not_happy_not_sad_will_raise_MoodAnalysisException(message):
    if 'happy' not in message or 'sad' not in message:
        raise MoodAnalysisException(code=102,msg=response[102])
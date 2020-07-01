from . validator import empty_message_raise_MoodAnalysisException, if_not_happy_not_sad_will_raise_MoodAnalysisException
from . exceptions import MoodAnalysisException
from . status import response

class MoodAnalyser:

    def analyseMood(self,message):
        try:
            empty_message_raise_MoodAnalysisException(message)
        except MoodAnalysisException as e:
            return {'msg':e.msg,'code':e.code}
        if 'happy' in message :
           return {'code':100,'msg':response[100]}
        elif 'sad' in message :
            return {'code':101,'msg':response[101]}
        return {'code':102,'msg':response[102]}
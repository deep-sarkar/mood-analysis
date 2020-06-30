from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from . status import response
from . serializers import MessageSerializer
from . validator import empty_message_raise_MoodAnalysisException, if_not_happy_not_sad_will_raise_MoodAnalysisException
from . exceptions import MoodAnalysisException

class MoodAnalyserView(GenericAPIView):
    serializer_class = MessageSerializer

    def post(self, request , *args , **kwargs):
        message = request.data.get('message')
        try:
            empty_message_raise_MoodAnalysisException(message)
        except MoodAnalysisException as e:
            return Response({'msg':e.msg,'code':e.code})
        if 'happy' in message :
           return Response({'code':100,'msg':response[100]})
        elif 'sad' in message :
            return Response({'code':101,'msg':response[101]})
        else:
            try:
                if_not_happy_not_sad_will_raise_MoodAnalysisException(message)
            except MoodAnalysisException as e:
                 return Response({'msg':e.msg,'code':e.code})


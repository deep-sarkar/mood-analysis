from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from . serializers import MessageSerializer
from . service import MoodAnalyser

class MoodAnalyserView(GenericAPIView):
    serializer_class = MessageSerializer

    def post(self, request , *args , **kwargs):
        message = request.data.get('message')
        refrence = MoodAnalyser()
        response = refrence.analyseMood(message)
        return Response(response)


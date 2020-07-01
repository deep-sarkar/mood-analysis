import pytest
from .. service import MoodAnalyser

class TestMoodAnalyser:
    def test_input_happy_mood_in_message_will_returns_100(self):
        message = 'I am happy today.'
        obj = MoodAnalyser()
        response = obj.analyseMood(message) 
        assert response['code'] == 100

    def test_input_sad_mood_in_message_will_returns_101(self):
        message = 'I am sad today.'
        obj = MoodAnalyser()
        response = obj.analyseMood(message) 
        assert response['code'] == 101
    
    def test_with_empty_message_will_raise_exception_and_returns_100(self):
        message = ''
        obj = MoodAnalyser()
        response = obj.analyseMood(message) 
        assert response['code'] == 100

    def test_without_mood_will_raise_exception_and_returns_102(self):
        message = 'hello there, how are you.'
        obj = MoodAnalyser()
        response = obj.analyseMood(message) 
        assert response['code'] == 102
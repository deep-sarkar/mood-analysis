import pytest
from .. import views
from django.test import RequestFactory
pytestmark = pytest.mark.django_db

class Test_MoodAnalyser:

    def test_if_mood_is_happy_returns_100(self):
        message = "I'm happy today." 
        req = RequestFactory().post('/',message)
        resp = views.MoodAnalyserView.as_view()(req) 
        assert resp.data['code'] == 101
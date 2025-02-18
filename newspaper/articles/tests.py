from django.test import TestCase
from django.urls import reverse
from .models import Article

class HomePageViewTest(TestCase):
    def setUp(self):
        Article.objects.create(text="another test")
    
    def test_view_url_exist_at_proper_location(self):

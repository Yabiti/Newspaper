from django.test import TestCase
from django.urls import reverse
from .models import Article

class HomePageViewTest(TestCase):
    def setUp(self):
        Article.objects.create(text="another test")
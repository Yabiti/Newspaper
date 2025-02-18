from django.test import SimpleTestCase, TestCase
from .models import Article
# Create your tests here.

class ArticleModelTest(TestCase):
    def setUp(self):
        Article.objects.create(text="just a test")
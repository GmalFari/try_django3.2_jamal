from django.test import TestCase
from .models import Articles
from django.utils.text import slugify
from .utils import slugify_instance_title
class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_articles = 5
        for i in range(0,self.number_of_articles):
            Articles.objects.create(title="hello world",content="something else")


    def test_query_exists(self):
        qs = Articles.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Articles.objects.all()
        self.assertEqual(qs.count(),self.number_of_articles  )
    def test_hello_world_slug(self):
        obj = Articles.objects.all().order_by("id").first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug,slugified_title)

    def test_slugify_instance(self):
        obj = Articles.objects.all().last()
        new_slugs = []
        for i in range(0,5):
            instance = slugify_instance_title(obj,save=False)
            new_slugs.append(instance.slug)
        unique_slugs = list(set(new_slugs))
        self.a

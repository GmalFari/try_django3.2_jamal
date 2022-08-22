from django.test import TestCase
from .models import Articles
from django.utils.text import slugify
from .utils import slugify_instance_title
class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_articles = 10
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
        self.assertEqual(len(new_slugs), len(unique_slugs))

    def test_slugify_instance_title_redux(self):
        slug_list = Articles.objects.all().values_list('slug',flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list),len(unique_slug_list)) 

    def test_article_search_manager(self):

        qs = Articles.objects.search(query="hello world")
        self.assertEqual(qs.count(),self.number_of_articles)
        qs = Articles.objects.search(query="hello world")
        self.assertEqual(qs.count(),self.number_of_articles)
        qs = Articles.objects.search(query='something else')
        self.assertEqual(qs.count(), self.number_of_articles)
    


    # def test_article_search_manager(self):
    #     qs = Article.objects.search(query='hello world')
    #     self.assertEqual(qs.count(), self.number_of_articles)
    #     qs = Article.objects.search(query='hello')
    #     self.assertEqual(qs.count(), self.number_of_articles)
    #     qs = Article.objects.search(query='something else')
    #     self.assertEqual(qs.count(), self.number_of_articles)
from django.test import TestCase
from blog.models import Post
from django.db.models.query import QuerySet


class PostTest(TestCase):

    def setUp(self):
        Post.objects.create(id="9b9325b9-6ed9-46d1-9499-92939b39ed62", title="IEEE XP", content="Programming", is_published=True)
        Post.objects.create(title="CCIS Open Day", content="lorm", is_published=True)
        Post.objects.create(title="Elections", content="Elections blog", is_published=False)

    def test_get_posts_exists(self):
        response = Post.get_posts()

        # Return type:
        self.assertEqual(type(response), QuerySet)
        self.assertEqual(response.model, Post)

        # Expected values:
        self.assertEqual(response.count(), 2)

    def test_get_posts_none(self):
        Post.objects.all().delete()
        response = Post.get_posts()

        # Return type:
        self.assertIsNone(response)

    def test_get_post_exists(self):
        response = Post.get_post("9b9325b9-6ed9-46d1-9499-92939b39ed62")
        # Return type:

        expected = "IEEE XP"
        self.assertEqual(response.title, expected)

from django.contrib.auth.models import User
from django.urls import resolve
from django.test import TestCase
from blog.views import post_list, post_detail, cv_detail, post_edit
from .models import Post, CV
from .forms import PostForm

# Create your tests here.
class HomePageTest(TestCase):

    def setUp(self):
        self.cv = CV.objects.create()

        self.username = 'test'
        self.password = 'password'
        self.user = User.objects.create_superuser(self.username, 'test@example.com', self.password)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'blog/base.html')
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertTemplateNotUsed(response, 'blog/post_detail.html')

    def test_post_create_and_edit(self):
        first_post = Post()
        first_post.title = 'test post'
        first_post.text = "text goes here"
        first_post.author = self.user
        first_post.save()
        response = self.client.get('/post/1/')
        self.assertNotEqual(response.status_code,404)
        self.assertContains(response, "test post")
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        response = self.client.get('/post/1/edit/')
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "text goes here")
        self.assertTemplateUsed(response, 'blog/post_edit.html')

    def test_404(self):
        response = self.client.get('/post/24/')
        self.assertEqual(response.status_code, 404)


    
    def test_post_url_resolves_to_post_detail_view(self):
        found = resolve('/post/1/')
        self.assertEqual(found.func, post_detail)

    #def test if view cv, edit cv, etc
    def test_cv_url_resolves_to_cv_page(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_detail)

    def test_cv_returns_correct_html(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'blog/cv_detail.html')
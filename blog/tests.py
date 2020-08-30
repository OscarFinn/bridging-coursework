from django.urls import resolve
from django.test import TestCase
from blog.views import post_list, post_detail

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'blog/base.html')
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertTemplateNotUsed(response, 'blog/post_detail.html')
    
    def test_post_url_resolves_to_post_detail_view(self):
        found = resolve('/post/1/')
        self.assertEqual(found.func, post_detail)

    #def test if view cv, edit cv, etc
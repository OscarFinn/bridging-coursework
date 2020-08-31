from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_a_blog_post_and_retrieve_later(self):
        #Enter blogging website
        #check homepage
        self.browser.get('https://oscarfinn.pythonanywhere.com')
        #header and title mentions this is oscars website
        self.assertIn('ofinn', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Oscar', header_text)
        #clicks on blog post

        #returns to home page

        #clicks on cv

        #sees the cv is there

        #goes to admin page and logs in
        self.browser.get('http://127.0.0.1:8000/admin/')

        #how do i test for blog posts being available from a user pov?
        self.fail('finish the test!')
if __name__ == '__main__':
    unittest.main(warnings='ignore')

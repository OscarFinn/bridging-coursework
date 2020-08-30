from selenium import webdriver
print ('working')
browser = webdriver.Firefox()
print ('working')
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title


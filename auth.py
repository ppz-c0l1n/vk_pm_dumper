#!usr/bin python
import mechanize



def vk_login(login, password):
     browser = mechanize.Browser()
     browser.addheaders = [('User-agent', 'Firefox')]
     browser.set_handle_robots(False)
     url = 'http://vk.com/login.php?email=' + login + '&pass=' + password
     browser.open(url)
     return browser

browser = vk_login('login', 'pass')
# 

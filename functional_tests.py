from selenium import webdriver

path = 'C:/Users/emilb/Documents/geckodriver.exe'
browser = webdriver.Firefox(executable_path=path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
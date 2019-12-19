from selenium import webdriver # c++의 using namespace와 동일
from selenium.webdriver.common.keys import Keys

#import bs4
#soup = bs4.BeautifulSoup()
#from bs4 import BeautifulSoup()
#soup = BeautifulSoup() # 주석처리한 위의 두 줄과 아래 두줄이 같음

path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.google.com/')
search_input = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search_input.send_keys('우워웡워워')
search_input.send_keys(Keys.RETURN)

#fakebox-input#fakebox-input
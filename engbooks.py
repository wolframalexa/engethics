# this script scrapes engineering book titles and descriptions from several of the main publishers,
# with the end goal of analyzing the identity of engineers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import requests
import time
from bs4 import BeautifulSoup as bs


f = open("descriptions.txt", "a")

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path='/mnt/c/Program Files (x86)/chromedriver.exe', chrome_options=option)

# open Princeton
browser.get('https://press.princeton.edu/books?search=&subjects%5B%5D=22606&subjects%5B%5D=22607&subjects%5B%5D=22608&subjects%5B%5D=22609&subjects%5B%5D=22610&subjects%5B%5D=114&subjects%5B%5D=22611&subjects%5B%5D=22612&subjects%5B%5D=22613&subjects%5B%5D=22614&subjects%5B%5D=22615&field_general_interest_value=All&field_on_sale_value=All&sort_by=field_book_published_date_value')

# click "load more" until no more books can be loaded
try:
	while browser.find_element_by_class_name("load-more"):
		btn = browser.find_element_by_class_name("load-more")
		browser.execute_script("arguments[0].click();", btn)
		time.sleep(8)
except NoSuchElementException:
	print("Finished loading page.")
	pass

book_list = browser.find_element_by_class_name("o-grid-listing")
book_items = book_list.find_elements_by_tag_name("li")
for book_item in book_items:
	link = book_item.find_element_by_tag_name("a").get_attribute("href")
	title = book_item.text
	data = requests.get(link).text

	soup = bs(data, 'html.parser')


	title = soup.find("h1", {"class": "o-book__title"})
	f.write(title.get_text())


	try:
		blurb = soup.find("div", {"class": "o-book__blurb f-landing"})
		f.write(blurb.get_text())

	except:
		pass

	try:
		body = soup.find("div", {"class": "o-book__body"})
		f.write(body.get_text())
	except:
		pass

	try:
		reviews = soup.find("div", {"class": "o-book__body-tab o-blocks o-blocks--reviews"})
		f.write(reviews.get_text())

	except:
		pass

browser.quit()
f.close()

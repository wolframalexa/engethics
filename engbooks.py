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
		print("clicked")
		time.sleep(8)
except NoSuchElementException:
	print("stopped")
	pass


# select list of all books
books = browser.find_elements_by_class_name("m-book-listing")
#links = books.find_elements_by_xpath("//a[@href]")

for element in books:
	link = element.find_element_by_xpath("//a[@class='m-book-listing__link']")
	print(link.get_attribute("href"))
#	url = "https://press.princeton.edu" + books.find_elements_by_xpath(".//a[@class='m-book-listing__link']"
#	i += 1
#	print(url)
#	data = requests.get(url).text
# parse using bs


# need to display all the books by hitting load more until it can't load any more
# grab the <ul> element
# iterate through child elements to get titles and links
# do requests.get to obtain description
# parse using beautifulsoup

#browser.quit()

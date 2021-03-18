# this script scrapes engineering book titles and descriptions from several of the main publishers,
# with the end goal of analyzing the identity of engineers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# open in incognito mode
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome(executable_path='/mnt/c/Program Files (x86)/chromedriver.exe', chrome_options=option)
browser.minimize_window()

# open Princeton
browser.get('https://press.princeton.edu/books?search=&subjects%5B%5D=22606&subjects%5B%5D=22607&subjects%5B%5D=22608&subjects%5B%5D=22609&subjects%5B%5D=22610&subjects%5B%5D=114&subjects%5B%5D=22611&subjects%5B%5D=22612&subjects%5B%5D=22613&subjects%5B%5D=22614&subjects%5B%5D=22615&field_general_interest_value=All&field_on_sale_value=All&sort_by=field_book_published_date_value')


# Wait 20 seconds for page to load
timeout = 20

# need to display all the books
# enter each book one by one to retrieve title, author, description (overview), praise (?)


try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
except TimeoutException:
    print('Timed out waiting for page to load')
    browser.quit()

# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath('//a[@class="text-bold"]')
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles:')
print(titles, '\n')

# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.support.ui import WebDriverWait

# pause = 10
# driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
# driver.get("your_url")
# #This code will scroll down to the end
# while True:
#     try:
#         # Action scroll down
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         break

#     except:     
#         pass

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
#C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver.get("https://store.steampowered.com/search/?specials=1")
urls = []
soup = BeautifulSoup(driver.page_source, "html.parser")


# for parent in soup.find_all(class_="y8HYJ-y_lTUHkQIc1mdCq _2INHSNB8V5eaWp4P0rY_mE"):
#     a_tag = parent.find("a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
#     base = "https://www.reddit.com/search/?q=covid19"
#     link = a_tag.attrs['href']
#     url = urljoin(base, link)
#     urls.append(url)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
#C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

class SteamDiscountItem:
    '''a national site

    Instance Attributes
    -------------------
    title: string
        the title of steam game (e.g. 'National Park', '')
  
    tag: string
    
    positive rate: string
        the city and state of a national site (e.g. 'Houghton, MI')

    discount rate: string
        the zip-code of a national site (e.g. '49931', '82190-0168')

    original price: string
        the phone of a national site (e.g. '(616) 319-7906', '307-344-7381')

    release date: string
        the name of a national site (e.g. 'Isle Royale')
    '''
    def __init__(self, title, tag, positive_rate, discount_rate,   original_price, discount_price, release_date):
        self.title = title
        self.tag = tag
        self.positive_rate = positive_rate
        self.discount_rate = discount_rate
        self.original_price = original_price
        self.discount_price = discount_price
        self.release_date = release_date

    def info(self):

        return "({}): {} {} {} {} {}".format(self.title, self.tag,
                                             self.positive_rate,
                                             self.discount_rate,
                                             self.original_price,
                                             self.discount_price,
                                             self.release_date)

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://store.steampowered.com/search/?specials=1&tags=492")

while True:
    try:
        # Action scroll down
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        break

    except:
        pass

soup = BeautifulSoup(driver.page_source, "html.parser")
rows = soup.find(id='search_resultsRows')
title = soup.find_all(class_='title')
positive_rate = soup.find_all(class_='search_review_summary positive')
discount_rate = soup.find_all(class_='col search_discount responsive_secondrow')
original_price = soup.find_all(class_='col search_price discounted responsive_secondrow')
release_date = soup.find_all(class_='col search_released responsive_secondrow')
# repeat n times
filter_number = soup.find_all(class_='search_results_filtered_warning')
fil = str(filter_number[0])
ind5 = fil.find("<div>")
ind6 = fil.find("results match your search")
n = int(fil[ind5+5:ind6].strip().replace(',',''))
# end of n

print(n)
print(len(soup))
print(len(rows))
print(len(title))
print(len(positive_rate))
print(len(discount_rate))
print(len(original_price))
print(len(release_date))



# itemList = []
# for i in range(n):
#     # title
#     title_v1 = str(title[n])
#     t = title_v1[20:-7]
#     # tag already exist
#     # positive_rate
#     #soup.find(class_='dropdown-menu')
#     pos_text = str(positive_rate[n])
#     ind = pos_text.find(";")
#     p = pos_text[ind+7:ind+10].strip()
#     # discount
#     d = discount_rate[n][-17:-14].strip('-')
#     #original price
#     price = str(original_price[n])
#     ind1 = price.find("<strike>")
#     ind2 = price.find("</strike>")
#     op = price[ind1+8:ind2]
#     # discount price
#     ind3 = price.find("<br/>")
#     ind4 = price.find("</div>")
#     dp = price[ind3+5:ind4]
#     # release date
#     dat = str(release_date[n])
#     rd = dat[53:-6]

#     it = SteamDiscountItem(t,"tag",p,d,op,dp,rd)
#     print(it.info())
#     print()



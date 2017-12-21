from selenium import webdriver
from bs4 import BeautifulSoup as bsp
import time

"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
"""


def getHtml(url, loadmore=False, waittime=10):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    times = 0
    while times < 5:
        ratio = 1/2
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight*{});".format(ratio))
        times += 1
    time.sleep(waittime)
    if loadmore:
        while True:
            try:
                next_button = browser.find_element_by_class_name("rate-paginator")
                next_button.click()
                time.sleep(waittime)
            except:
                break
    html = browser.page_source
    browser.quit()
    return html

# for test taobao 枸杞
url = "https://detail.tmall.com/item.htm?id=6956495372&ali_refid=a3_430583_1006:1102965417:N:%E6%9E%B8%E6%9D" \
      "%9E:5f4c1d6fca0d0ee5543b27796f7b6b26&ali_trackid=1_5f4c1d6fca0d0ee5543b27796f7b6b26&spm=a230r.1.14.1"
html = getHtml(url)
# get by attributes
rs = bsp(html, "html.parser")
# output the review
for item in rs.select('.tm-rate-fulltxt'):
    print(item)

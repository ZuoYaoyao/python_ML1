import expanddouban as exp
import operator
from bs4 import BeautifulSoup as soup

import csv

location_arg = ['大陆', '美国', '香港', '台湾', '日本',
                '韩国', '英国', '法国', '德国', '意大利',
                '西班牙', '印度', '泰国', '俄罗斯', '伊朗',
                '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西',
                '丹麦']

type_arg = ['喜剧', '悬疑', '励志']

location_dict = {'大陆': 0, '美国': 0, '香港': 0, '台湾': 0, '日本': 0, '韩国': 0,
                 '英国': 0, '法国': 0, '德国': 0, '意大利': 0, '西班牙': 0,
                 '印度': 0, '泰国': 0, '俄罗斯': 0, '伊朗': 0, '加拿大': 0,
                 '澳大利亚': 0, '爱尔兰': 0, '瑞典': 0, '巴西': 0, '丹麦': 0}
statistic = []
cat_count = []


# task1
def get_movie_url(category, location):
    url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags='
    # append args
    url = url + category + ',' + location
    return url


# task2
"""
import requests
response = requests.get(url)
html = response.text
"""


# task3
class Movie:
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

    def print_data(self):
        return "{},{},{},{},{},{}".format(self.name, self.rate, self.location, self.category, self.info_link,
                                          self.cover_link)


# task4
"""
return a list of Movie objects with the given category and location.
自选种类，所有地区3*21=63
"""


def getMovies(category, location):
    result_list = []
    for cat in category:
        tmp_count = 0
        for loc in location:
            # step1: get url
            url = get_movie_url(cat, loc)
            #print(url)
            # step2: get html
            html = exp.getHtml(url, True)
            # step3: convert by soup
            result = soup(html, 'html.parser')
            #print(location_dict[loc])
            # clear
            location_dict[loc] = 0
            # loop
            for item in result.find(id='content').find(class_='list-wp').find_all('a'):
                title = item.find(class_='title').string
                rate = item.find(class_='rate').string
                item_url = item.get("href")
                pic_url = item.find('img').get('src')
                ob = Movie(title, rate, loc, cat, item_url, pic_url)

                location_dict[loc] += 1
                tmp_count += 1
                result_list.append(ob)
            #print(location_dict[loc])
        cat_count.append(tmp_count)
        # for item in result_list:
        # print(item.name)
        # sort dict by value
        sorted_x = sorted(location_dict.items(), key=operator.itemgetter(1), reverse=True)
        # select top 3
        tmp_list = []
        tmp_list.append(sorted_x[0])
        tmp_list.append(sorted_x[1])
        tmp_list.append(sorted_x[2])
        statistic.append(tmp_list)

    return result_list


output = getMovies(type_arg, location_arg)
# task5
"""
自选种类，所有地区3*21=63
format: [name,rating,district,genre,url,img_url]
movies.csv主要是写入csv
"""

with open('movies.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, escapechar='\\')
    for item in output:
        # print(item.name)
        # replace char which can't be written to csv
        #name = item.name.encode("gbk", "replace").decode("gbk")
        spamwriter.writerow([item.name, item.rate, item.location, item.category, item.info_link, item.cover_link])

# task6
"""
简单统计
"""

"""
for item in cat_count:
    print(item)
for item in statistic:
    print(item)

for item in statistic:
    for it in item:
        print(it)
"""

with open('output.txt', 'w', encoding='utf-8-sig') as txt:
    index = 0
    for cat in type_arg:
        txt.write(cat)
        txt.write('\t')
        txt.write('比例')
        txt.write('\n')
        for it in statistic[index]:
            ratio = round(it[1] / cat_count[index] * 100, 2)
            percent = str(ratio) + '%'

            txt.write(it[0])
            txt.write('\t')
            txt.write(percent)
            txt.write('\n')
        index += 1
        txt.write('\n')

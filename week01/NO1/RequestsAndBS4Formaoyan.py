import requests
from bs4 import BeautifulSoup as bs
import pandas

url = 'https://maoyan.com/films?showType=3'
Accept_Language = 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'

# 声明为字典使用字典的语法赋值
header = {}
header['Accept'] = 'image/webp,*/*'
header['user-agent'] = user_agent
header['Accept-Language'] = Accept_Language
response = requests.get(url, headers=header)

bs_info = bs(response.text, 'html.parser')
#print(response.text)

mFilmList = []
for mItem in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    if len(mFilmList) <= 10:
        film_name = mItem.find('span', attrs={'class': 'name'}).text
        hover_tags = mItem.find_all('span', attrs={'class': 'hover-tag'})
        film_type = hover_tags[0].next_sibling.strip()
        plan_date = hover_tags[2].next_sibling.strip()
        mFilmStr = '名称：' + film_name.strip() + '；' + '类型：' + film_type.strip() + '；' + '上映时间：' + plan_date.strip() + '；'
        mFilmList.append(mFilmStr)
    else:
        break

mFilmFrame = pandas.DataFrame(data=mFilmList)
mFilmFrame.to_csv('./FilmList.csv', encoding='gbk',index=False, header=False)

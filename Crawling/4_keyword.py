"""
날짜 : 2021/06/08
이름 : 고현석
내용 : 파이썬 실시간 검색어 크롤링 실습하기
"""

import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

response = req.get('https://issue.zum.com/')

dom = bs(response.text, 'html.parser')
divs = dom.select('#issueKeywordList > li > div.cont')
#디렉토리 생성

# 파일생성
dir = "./keyword/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    # 해당 디렉토리가 존재하지 않으면
    os.makedirs(dir)

fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# 파일저장
file.write('랭킹,검색어\n')
for div in divs:
    rank = div.find(class_='num').text
    word = div.find(class_='word').text

    file.write('%s,%s\n' %(rank[:-1],word))

file.close()

# 네이터(줌) 실시간 검색어 수집
# 1분마다 한번 Crawler 실행
# 수집 데이터 파일로 저장

import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

response = req.get('https://issue.zum.com/')

dom = bs(response.text, 'html.parser')
divs = dom.select('#issueKeywordList > li > div.cont')
#디렉토리 생성


dir = "./keyword/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    # 해당 디렉토리가 존재하지 않으면
    os.makedirs(dir)

# 파일생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# 파일저장
file.write('랭킹,검색어\n')
for div in divs:
    rank = div.find(class_='num').text #랭킹값
    word = div.find(class_='word').text #검색어값

    file.write('%s,%s\n' %(rank[:-1],word))

file.close()
import datetime
import requests
import bs4
현재=str(datetime.datetime.now())
print(현재)
날=현재[:4]+현재[5:7]+현재[8:10]
print(날)

html=requests.get('http://school.cbe.go.kr/gakri-e/M01190505/list?ymd=20201030'+날)
# print(html.text)

수프=bs4.BeautifulSoup(html.text,'html.parser')
# print(수프)

트롤=수프.find('a', href='/gakri-e/M01190505/list?ymd='+날)
# print(트롤)
식단리스트=트롤.find_all('li')
# print(식단리스트)
식단=''
for i in 식단리스트:
    식단=식단+i.text+'\n'

import telegram
토큰='1401274407:AAFt16tUDwT2cJRmYfh-kVicWUY5VGcjLVE'
봇=telegram.Bot(token=토큰)

for i in 봇.getUpdates():
    print(i.message)
봇.sendMessage('1401132321',식단)
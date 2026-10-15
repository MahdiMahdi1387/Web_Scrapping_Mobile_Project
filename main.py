from bs4 import BeautifulSoup as bs
import requests as rq
from db_management import Database_control

db = Database_control()
db.init()

url = 'https://www.technolife.com/category/mobile/mobile-phone'
response = rq.get(url, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"
})
soup = bs(response.text, 'html.parser')

cards = soup.select('section.relative.w-full.rounded-\\[10px\\].bg-white')

i = 1
for card in cards:
    description: str = card.select_one('h2.yekanbakh-en.line-clamp-3.h-\\[75px\\].' \
    'overflow-hidden.text-sm.font-medium.leading-6\\.5.' \
    '-tracking-0\\.5.text-gray-800').get_text()
    splited_desc: list[str] = description.split(' ') # splited descrpition by space ' '

    brand: str = splited_desc[2]

    memory: str = card.select_one('p.yekanbakh-en.text-xs.font-semiBold.' \
    'leading-4.text-gray-700').get_text()

    if memory is None:
        continue

    if splited_desc[-1] == 'ویتنام' and \
        splited_desc[-2] == '-':
        for _ in range(2):
            splited_desc.pop()
    if splited_desc[-1] != 'گیگابایت':
        continue

    ram: str = splited_desc[-2] + ' ' + splited_desc[-1]

    rating: float = float(card.select_one('p.text-sm.font-semiBold.' \
    'leading-\\[18px\\].text-gray-600').get_text())

    print(db.add(i, description, brand, memory, ram, rating))

    i += 1

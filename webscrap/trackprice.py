#track price of the particular product if the price of the product drop then it will automatically get us to the website
import requests as r
from bs4 import BeautifulSoup as bs
import time
import webbrowser as ws
url="https://www.flipkart.com/asus-zenfone-5-a501cg-gold-8-gb/p/itmeuydansgfvjtp?pid=MOBDXZ9W7DHYYWEP&lid=LSTMOBDXZ9W7DHYYWEPCKFKLU&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=d1fd1cd8-6a38-4613-a7b6-d530a6d45e6e.MOBDXZ9W7DHYYWEP.SEARCH&ppt=sp&ppn=sp&ssid=noluofxkts0000001591085408975&qH=936aa2d51122f827"
while True:
    page=r.get(url)
    soup=bs(page.content,'html.parser')
    title=soup.title.text
    print("\n",title)
    price=soup.find("div",{"class":"_1vC4OE _3qQ9m1"}).text
    price=price[1:]
    price_ar=price.split(",")
    price="".join(price_ar)
    price=int(price)
    print(price)
    if price<10000:
        ws.open(url)
    time.sleep(5)
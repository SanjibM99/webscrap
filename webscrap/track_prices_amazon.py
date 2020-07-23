import requests
from bs4 import BeautifulSoup
import smtplib

def send_email():
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("<your email id>","<your email password>")
    server.sendmail("<your email/sender>","<reciever email>","price is dropped")
    server.quit()


page_url="https://www.flipkart.com/dell-14-3000-core-i3-7th-gen-4-gb-1-tb-hdd-linux-inspiron-3481-laptop/p/itm466e453c2270b?pid=COMFHTHRNDH3EZ2E&lid=LSTCOMFHTHRNDH3EZ2EIQDJT3&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Flipstart%2BDeals%2BOf%2BThe%2BDay_1_3.dealCard.OMU_Flipstart%2BDeals%2BOf%2BThe%2BDay_XNCRGB3PXXOL_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Flipstart%2BDeals%2BOf%2BThe%2BDay_NA_dealCard_cc_1_NA_view-all_2&fm=neo%2Fmerchandising&iid=041744ad-03de-4782-a87b-403651dd6744.COMFHTHRNDH3EZ2E.SEARCH&ppt=browse&ppn=browse&ssid=h95r886cao0000001591087866224"
brower_agent={"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
product_page=requests.get(page_url,headers=brower_agent)
soup=BeautifulSoup(product_page.content,'html.parser')
#print(soup.prettify())
page_title=soup.find("span",class_="_35KyD6").text
print(page_title)
price_tag=soup.find("div",{"class":"_1vC4OE _3qQ9m1"}).text
price_tag=price_tag[1:]
price_ar=price_tag.split(",")
price="".join(price_ar)
price=int(price)
print(price)
if(price<=26990):
    send_email()



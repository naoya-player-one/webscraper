from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen
import csv
import pickle


ranges = range(1,100)

href_data = []

for eachp in ranges:

    try:
        html=urlopen("http://global.rakuten.com/en/category/110729/?p="+str(eachp)+"&l-id=rgm-top-en-nav-women-onepiece")
        
    except HTTPError as e:
        print(e)

    except URLError as e:
        print(e)
        
    else:
        print("It worked", str(eachp))

    bsObj = bs(html,"lxml")

    divs=bsObj.findAll("div",{"class":"b-content b-text-overflow b-text-small b-text-sub"})

    for link in divs:
        if link not in href_data:
            href_data.append(link)
        else:
            pass

shop_urls = []

for shop in href_data:
    shop_url="http://global.rakuten.com"+shop.find("a").get("href")+"info.html"
    shop_urls.append(shop_url)

pickle_out = open('company_profile_women_onepiece.pickle','wb')
pickle.dump(shop_urls,pickle_out)
pickle_out.close()

for profile_page in shop_urls:
    try:
        html = opener.open(profile_page)

    except HTTPError as e:
        print(e)

    except URLError as e:
        print(e)
        
    else:
        print("Found profile page")


    try:
        bsObj = bs(html, "html5lib")
        info_list = bsObj.find_all("div",{"class":"c-spCompanyInner"})[0]

    
        company_name = info_list.h1.text
        address = info_list.find_all("dd")[0].get_text(strip=True)
        telephone = info_list.find_all("dd")[1].get_text(strip=True)
        rep = info_list.find_all("dd")[2].get_text(strip=True)
        email_address = info_list.find_all("dd")[5].get_text(strip=True)

##        company_info.append([company_name,address,rep,telephone,email_address])
        company_info = [[company_name,address,rep,telephone,email_address,profile_page]]

        with open("company_information_sake.txt","a") as csvfile:
##             fieldnames = [['会社名', '住所',"電話番号","代表者","e-mail"]]
             writer = csv.writer(csvfile)
##             writer.writerows(fieldnames)
             writer.writerows(company_info)
             csvfile.close()
        
    except IndexError:
        print("IndexError")

    except AttributeError:
        print("AttributeError")

##company_info = []
##
##for profilep in shop_urls:
##    try:
##        html=urlopen(profilep)
##        
##    except HTTPError as e:
##        print(e)
##
##    except URLError as e:
##        print(e)
##        
##    else:
##        print("Found profile page")
##
##    info =shop_info.find_all("div",{"class":"c-spCompanyInner"})
##    if len(info)>0:
##        company_info.append(info[0])
##    else:
##        pass
##    

    
##    shop_info = bs(urlopen(shop_url),"lxml")
##    
##    info = shop_info.find_all("div",{"class":"c-spCompanyInner"})
##
##    if info is not None:
##        company_info.append(info[0])
##    else:
##        pass

    

##company_info_string = []
##for company in company_info:
##
##    company_name = company.find("dt").get_text()
##    address = company.find_all("dd")[0].get_text()
##    tel = company.find_all("dd")[1].get_text()
##    rep = company.find_all("dd")[2].get_text()
##    rep2 = company.find_all("dd")[3].get_text()
##    rep3 = company.find_all("dd")[4].get_text()
##    contact = company.find_all("dd")[5].get_text()
##
##    company_info_string = {"会社名":{




    
    


    

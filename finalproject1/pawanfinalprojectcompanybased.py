

import os,random,sys,time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

browser=webdriver.Chrome('driver/chromedriver.exe')

browser.get('https://www.linkedin.com/uas/login') 

print("Enter mail id:")
username=input()
print("Enter password:")
password=input()


elementID=browser.find_element(By.ID,'username')
elementID.send_keys(username)
elementID=browser.find_element(By.ID,'password')
elementID.send_keys(password)
elementID.submit()


print("Enter the scroll pause time:")
SCROLL_PAUSE_TIME=int(input())



from bs4 import BeautifulSoup
# from lxml import html,etree
import pandas as pd
import json



from typing import List
import urllib




def soup_fetch(url:str):
    browser.get(url)
    
    # browser.execute_script("window.open('about:blank','secondtab');")
    # browser.switch_to.window("secondtab")
    # browser.get('https://www.linkedin.com/in/pawan-kumar-sharma-b179621bb/details/skills/')
    # browser.get(link)
    SCROLL_PAUSE_TIME=10
    last_height=browser.execute_script('return document.body.scrollHeight')
    
    for i in range(5):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(SCROLL_PAUSE_TIME)
        new_height=browser.execute_script('return document.body.scrollHeight');
        if new_height==last_height:
            break
        last_height=new_height

    src=browser.page_source
    soup=BeautifulSoup(src,'lxml')
    
    return soup


print("Enter the url:")
url=input()

print("Enter the value of end page (should be greater than 1):")
last=int(input())


def search_people() -> List[str]:
#     encodeName = urllib.parse.quote(name)
    full_links=[]
    for p in range(1,last):
        time.sleep(SCROLL_PAUSE_TIME)
        print("--------------")
        print(url.format(p=p))
        print("--------------")
        # url=f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102713980%22%5D&companySize=%5B%22D%22%5D&industry=%5B%224%22%5D&origin=FACETED_SEARCH&page={p}'
        searchPageSoup = soup_fetch(url.format(p=p))
        span_tags = searchPageSoup.find_all('span',{'class':'t-16'})
        links = [span.find('a',{'class':'app-aware-link'}).get('href') for span in span_tags ]
        full_links +=links
#     return links
    return full_links





def soup_fetch(url:str):
    browser.get(url)
    
    
    
    last_height=browser.execute_script('return document.body.scrollHeight')
    
    for i in range(5):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(SCROLL_PAUSE_TIME)
        new_height=browser.execute_script('return document.body.scrollHeight');
        if new_height==last_height:
            break
        last_height=new_height

    src=browser.page_source
    soup=BeautifulSoup(src,'lxml')
    
    return soup




some_links = search_people()
some_links 

count=len(some_links)
print("------------------")
print(count)
print("------------------")








def fetch_full_data(url:str) -> dict[str,str]:
#     data_soup =  soup_fetch(url)
    skill_soup =  soup_fetch(f'{url}about/')
    
    
    
    list = skill_soup.find('dl', {'class': 'overflow-hidden'}).find_all(['dd', 'dt'])
    overview=skill_soup.find('p',{'class':'break-words white-space-pre-wrap mb5 text-body-small t-black--light'}).get_text().strip()

    data_map = {'Overview': overview}
    key = None
    for item in list:
        item_string = str(item)
        text = item.get_text().strip()
        if (item_string.startswith('<dt')):
            key = text
        else:
            if (key in data_map):
                data_map[key] += ' ' + text
            else:
                data_map[key] = text
    return data_map



def soup_fetch(url:str):
    browser.get(url)
    
    
    SCROLL_PAUSE_TIME=10
    last_height=browser.execute_script('return document.body.scrollHeight')
    
    for i in range(5):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(SCROLL_PAUSE_TIME)
        new_height=browser.execute_script('return document.body.scrollHeight');
        if new_height==last_height:
            break
        last_height=new_height

    src=browser.page_source
    soup=BeautifulSoup(src,'lxml')
    
    return soup




final_list= []
for abc in some_links:
    final_list.append(  fetch_full_data(abc))





final_list


df = pd.DataFrame(final_list)
df

df.to_csv('act21projectfinal32.csv',index=False)








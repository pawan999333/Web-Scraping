

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
import pandas as pd
import json



from typing import List
import urllib




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




    
   
    





# def soup_fetch(url:str):
    browser.get('https://www.linkedin.com/company/fintree-finance/about/')
    
    
    
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













# def fetch_full_data(url:str) -> dict[str,str]:
#     data_soup =  soup_fetch(url)
    skill_soup =  soup_fetch('https://www.linkedin.com/company/fintree-finance/about/')
    
    
    
    list = skill_soup.find('dl', {'class': 'overflow-hidden'}).find_all(['dd', 'dt'])
    try:
        overview=skill_soup.find('p',{'class':'break-words white-space-pre-wrap mb5 text-body-small t-black--light'}).get_text().strip()
    except:
        pass
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






final_list


df = pd.DataFrame(final_list)
df

df.to_csv('act21projectfinal32.csv',index=False)








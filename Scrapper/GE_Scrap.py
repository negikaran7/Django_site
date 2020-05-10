# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:00:24 2020

@author: DINES
"""

import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

# os.chdir("C:\\Users\\DINES\\Desktop\\Development\\GE_Scrap\\")
driver = webdriver.Chrome('chromedriver\\81\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.devex.com/login')
#========================================================
def get_elemet_att(web_driver,element_att,ret_arr=False):  
    # Link: partial/Full Link Text
    # ID: element ID
    # CLASS: element class
    # default is xpath
    if element_att.upper().startswith("LINK"):
        ele_find=web_driver.find_elements_by_partial_link_text(element_att.split(":")[1])
    elif element_att.upper().startswith("ID"):
        ele_find=web_driver.find_elements_by_id(element_att.split(":")[1])
    elif element_att.upper().startswith("NAME"):
        ele_find=web_driver.find_elements_by_name(element_att.split(":")[1])
    elif element_att.upper().startswith("CLASS"):
        ele_find=web_driver.find_elements_by_class_name(element_att.split(":")[1])
    else:
        ele_find=web_driver.find_elements_by_xpath(element_att)
    if len(ele_find)>0:
        if ret_arr==True:
            return ele_find
        else:
            return ele_find[0]
    else:
        return None

def write_value(element_obj,txt_to_write):
    element_obj.clear()
    element_obj.send_keys(txt_to_write)

def add_to_dict(dictionary, key, value):
    key=key.lower()
    if type(value)==list:
        for val in value:
            add_to_dict(dictionary,key,val)
    else:
        if key not in dictionary:
            dictionary[key] = [value]
        elif type(dictionary[key]) == list:
            dictionary[key].append(value)
        else:
            dictionary[key] = [dictionary[key], value]

def add_ele_dict_title(result_in,dict_titles,tmp_dict):  
        for dict_ttl in dict_titles:
            dict_ttl_key=dict_ttl.upper()
            if dict_ttl_key in tmp_dict.keys():
                add_to_dict(result_in,dict_ttl_key,tmp_dict[dict_ttl_key])
            else:
                add_to_dict(result_in,dict_ttl_key,"")

def get_second_lvl(driver,result_in):
    ele_len=0
    while ele_len==0:    
        time.sleep(1)
        detail_info=driver.find_element_by_class_name('other-info')
        ele=detail_info.find_elements_by_tag_name('li')
        ele_len=len(ele)
    info_dict={}
    info_titles=['Tendering Organization','Opportunity Size','Value','Deadline','Categories','Topics','Reference Number']
    for ind in range(0,len(ele)):        
        ele_txt=ele[ind].get_attribute('innerText').splitlines()
        info_dict[ele_txt[0].upper()]=ele_txt[1]
#        add_to_dict(result_in,ele_txt[0],ele_txt[1])
    add_ele_dict_title(result_in,info_titles,info_dict)
        
    time_line_info=driver.find_elements_by_class_name('detail-timeline')
    date_dict={}
    date_titles=['ANNOUNCED ON','FUNDING APPROVED ON','START DATE','END DATE','GRANT ANNOUNCED ON','DEADLINE','EXPECTED DATE OF APPROVAL','EXPECTED END'
    ]
    if len(time_line_info)>0:
        time_line_info=time_line_info[0]
        dates_ele=time_line_info.find_elements_by_class_name('row')
        for date_ in dates_ele:        
            date_key=date_.find_element_by_class_name('text-gray-li').get_attribute('innerText')
            date_val=date_.find_element_by_class_name('date').get_attribute('innerText')
            date_dict[date_key.upper()]=date_val
    add_ele_dict_title(result_in,date_titles,date_dict)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
user_name=get_elemet_att(driver,"id:login")
write_value(user_name,'akanksha.kapoor@ge.com')
user_name=get_elemet_att(driver,"id:password_text")
write_value(user_name,'Covid19GE')
login_btn=get_elemet_att(driver,'//*[@id="login-form"]/button')
login_btn.click()
#driver.execute_script('arguments[0].scrollIntoView(true);', login_btn)
time.sleep(2)
funding_tab=get_elemet_att(driver,'linktext:Funding')
time.sleep(2)
funding_tab.click()
time.sleep(2)

funding_search=get_elemet_att(driver,'//*[@id="search-bar"]/div[1]/div[1]/div/div/div/input')
write_value(funding_search,'COVID')
src_btn=get_elemet_att(driver,'//*[@id="search-bar"]/div[1]/div[1]/div/div/div/span/button')
src_btn.click()
time.sleep(2)
result_out={}

for page_index in range(0,15):
    i=1
    time.sleep(4)
    result_div=get_elemet_att(driver,'class:search-results')
    res_div_eles=result_div.find_elements_by_class_name('link-blue-orange')
    for result_div_ele in res_div_eles:
        time_frame=result_div_ele.find_element_by_class_name('top').get_attribute('innerText')
        typ_text=result_div_ele.find_element_by_class_name('status').get_attribute('innerText')
        title=result_div_ele.find_element_by_class_name('title').get_attribute('innerText')
        donor=result_div_ele.find_element_by_class_name('funder').get_attribute('innerText')
        location=result_div_ele.find_element_by_class_name('location').get_attribute('innerText')
        
        add_to_dict(result_out,'Time_Posted',time_frame)
        add_to_dict(result_out,'Type',typ_text)
        add_to_dict(result_out,'Title',title)
        add_to_dict(result_out,'Donor',donor)
        add_to_dict(result_out,'Location',location)
        driver.execute_script('arguments[0].scrollIntoView(true);', result_div_ele)
        result_div_ele.click()
        time.sleep(1)
        print( 'extracting for ' + str(page_index) + ' result id ' + str (i))
        i=i+1
        get_second_lvl(driver,result_out)
    nxt_btn_ele=driver.find_element_by_class_name('next-button-link')
    driver.execute_script('arguments[0].scrollIntoView(true);', nxt_btn_ele)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight +100);')
    nxt_btn_ele.click()
print('finished')
del result_out['deadline']
data_out=pd.DataFrame.from_dict(result_out)
data_out.to_csv('output/devex.csv')

driver.get('https://sciencebusiness.net/sciencebusiness-database-coronavirus-funding-opportunities')
driver.switch_to.frame(0)
eleTbl=driver.find_element_by_class_name('waffle')
tblHTML=eleTbl.get_attribute("outerHTML")
soup=BeautifulSoup(tblHTML,'html.parser')
dfOut=pd.read_html(tblHTML,header=2)[0]
dfOut=dfOut.dropna(axis=1,how='all')
dfOut.to_csv('science_business.csv',index=False)

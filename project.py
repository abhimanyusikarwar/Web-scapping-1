from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/Users/mahen/OneDrive/Desktop/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

stars_data = []


def scrape():

    for i in range(0,1):
        soap = BeautifulSoup(browser.page_source, "html.parser")
        for th_tag in soap.find_all("th", attrs={"class", "stars"}):

            tr_tags = th_tag.find_all("tr")
           
            temp_list = []

            for index, tr_tag in enumerate(tr_tags):

                if index == 0:                   
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")

            stars_data.append(temp_list)

        
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


scrape()


headers = ["Proper name","Distance","Mass","Radius"]


stars_df_1 = pd.DataFrame(stars_data, columns=headers)


stars_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
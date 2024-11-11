from bs4 import BeautifulSoup
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def find_porssi_teams():
    print('hello world')

    url = 'https://www.liiga.fi/fi/pelaajat?kausi=2024-25&sarja=runkosarja'
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(3)

    cookies = driver.find_element(By.CLASS_NAME,'qc-cmp2-summary-buttons')
    print(cookies)
    accept_button = cookies.find_element(By.CLASS_NAME,'css-47sehv')
    
    ActionChains(driver).click(accept_button).perform()
    time.sleep(3)
    html = driver.page_source
    

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('div', class_='_tableContainer_1a9ud_170 _sairaSemiCondensed_1a9ud_5 _fontSize15_1a9ud_84 _shadowRight_1a9ud_141')
    print(table)
   # print(soup)

    driver.close()
def main():
    find_porssi_teams()

if __name__ == '__main__':
    main()
from bs4 import BeautifulSoup
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def find_matches():
    url = 'https://www.flashscore.com/hockey/finland/liiga/#/WY20QoqE/table/overall'
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    time.sleep(5)
    driver.close()

    soup = BeautifulSoup(html, 'html.parser')

    match_table = soup.find('div', class_='sportName hockey')

    event_link_html_object = match_table.find_all('a', class_='eventRowLink')
    match_time_html_object = match_table.find_all('div', class_='event__time')
    match_home_team_html_object = match_table.find_all('div', class_='event__participant event__participant--home')
    match_away_team_html_object = match_table.find_all('div', class_='event__participant event__participant--away')

    i = 0
    match_details_list = []
    while i < len(match_time_html_object):
        match_time = match_time_html_object[i].text
        home_team = match_home_team_html_object[i].text
        away_team = match_away_team_html_object[i].text
        match_link = event_link_html_object[i]['href']

        row = [match_link, match_time, home_team, away_team]
        match_details_list.append(row)
        i += 1

    print(match_details_list)

def main():
    find_matches()

if __name__ == '__main__':
    main()
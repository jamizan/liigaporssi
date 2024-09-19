from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def FindCurrentMatches():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url = 'https://www.flashscore.com/nhl-2023-2024/results/'
    driver.get(url)

    time.sleep(5)

    html = driver.page_source

    driver.quit()

    page = BeautifulSoup(html, 'html.parser')

    matchInfo = page.find_all('div', class_='event__match event__match--withRowLink event__match--static event__match--twoLine')


    length = len(matchInfo)
    x = 0
    returnData = []
    
    while x < length:
        row = []

        matchDate = matchInfo[x].find('div').text

        eventDate = matchDate[0:5]

        eventTime = matchDate[7:12]

        if eventDate == '19.04':
                    
            matchId = matchInfo[x]['id']
            matchId = matchId.replace('g_4_', '')

            link = 'https://www.flashscore.com/match/'+ matchId +'/#/match-summary/player-statistics/0'

            homeTeam = matchInfo[x].find('div', class_='event__participant event__participant--home')
            awayTeam = matchInfo[x].find('div', class_='event__participant event__participant--away')

            if homeTeam == None:
                homeTeam = matchInfo[x].find('div', class_='event__participant event__participant--home fontExtraBold')
            if awayTeam == None:
                awayTeam = matchInfo[x].find('div', class_='event__participant event__participant--away fontExtraBold')

            row = [matchId, link, eventDate, eventTime, homeTeam.text, awayTeam.text]

            returnData.append(row)

            x += 1
        else:
            x += 1
        
            

    print(returnData)
    return returnData


    

def MainScrapeFunction():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = "https://www.flashscore.com/match/ro9gcXlC/#/match-summary/player-statistics/0"
    driver.get(url)

    time.sleep(5)

    html = driver.page_source


    driver.quit()


    page = BeautifulSoup(html, 'html.parser')


    StatTable = page.find(class_='section psc__section')

    rows = StatTable.find_all("div", {"class":"ui-table__row playerStatsTable__row"})

    PlayerDataByRow = []


    for row in rows:
        RowData = []
        cols = row.find_all(["div", {"class":"playerStatsTable__cell"}])
        for col in cols:
            if col.get_text(strip=True) == '-':
                RowData.append(0)
            else:
                RowData.append(col.get_text(strip=True))
                if len(RowData) < 15:
                    continue
                else:
                    PlayerDataByRow.append(RowData)


    return PlayerDataByRow

def main():

    PlayerDataByRow = MainScrapeFunction()
    print(PlayerDataByRow)
    return PlayerDataByRow

#    FindCurrentMatches()
if __name__ == '__main__':
    main()

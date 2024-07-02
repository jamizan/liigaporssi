from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

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

if __name__ == '__main__':
    main()

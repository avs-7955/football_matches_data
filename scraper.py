from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'D:\VIT\Self_Dev\CODING\Web Scraping\chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

all_matches_btn = driver.find_element(By.XPATH,
                                      '//label[@analytics-event="All matches"]')
all_matches_btn.click()


matches = driver.find_elements(By.TAG_NAME, 'tr')
date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)
driver.quit()

df = pd.DataFrame({'Date': date, 'HomeTeam': home_team,
                  'Score': score, 'AwayTeam': away_team})
df.to_excel('football_scores.xlsx', 'All matches', index=False)
# df.to_csv('football_matches', index=False)


# time.sleep(5000)

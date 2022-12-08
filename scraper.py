from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Website containing data about Football Matches
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'

# Chrome Driver path
path = 'D:\VIT\Self_Dev\CODING\Web Scraping\chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

# Clicking the all matches btn
all_matches_btn = driver.find_element(By.XPATH,
                                      '//label[@analytics-event="All matches"]')
all_matches_btn.click()

# Finding the rows of the table
matches = driver.find_elements(By.TAG_NAME, 'tr')

# Creating empty lists and appending items to it
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

# Creating a data frame and stroring the data into excel file
df = pd.DataFrame({'Date': date, 'HomeTeam': home_team,
                  'Score': score, 'AwayTeam': away_team})
df.to_excel('football_scores.xlsx', 'All matches', index=False)

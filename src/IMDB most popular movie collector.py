from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
import re

def time_to_minutes(time_str):
    total_minutes = 0
    parts = time_str.split()
    for part in parts:
        if 'h' in part:
            total_minutes += int(part.strip('h')) * 60
        elif 'm' in part:
            total_minutes += int(part.strip('m'))
    return total_minutes

def clean_rating_amount(rate_amount_text):
    # Remove parentheses, spaces, and 'K'
    cleaned_text = rate_amount_text.replace('(', '').replace(')', '').replace(' ', '').replace('K', '')
    # Convert to integer
    if cleaned_text.isdigit():
        return int(cleaned_text)
    else:
        return 0

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
driver.get(url)

# Find elements for each group
movie_titles = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/div[2]/a/h3')
movie_years = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/div[3]/span[1]')
movie_lengths = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/div[3]/span[2]')
movie_rates = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/span/div/span')
movie_rate_amounts = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/span/div/span/span')
movie_group = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/div[3]/span[3]')

# Determine minimum length of lists
min_length = min(len(movie_titles), len(movie_years), len(movie_rates), len(movie_lengths), len(movie_rate_amounts), len(movie_group))

data = []
for i in range(min_length):
    title = movie_titles[i].text
    year = movie_years[i].text
    rate_text = movie_rates[i].text.split('\n')[0]  # Extract only the first number from rating
    length = time_to_minutes(movie_lengths[i].text)  # Convert time to minutes
    rate_amount_text = movie_rate_amounts[i].text.strip()  # Extract rate amount
    rate_amount = clean_rating_amount(rate_amount_text)  # Clean and convert rate amount
    group = movie_group[i].text.strip()  # Extract group information

    data.append([title, year, rate_text, length, rate_amount, group])

driver.quit()

# Write data to CSV file
csv_filename = 'imdb_movies.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'Year', 'Rating', 'Duration (minutes)', 'Rating Amount', 'Group'])
    csvwriter.writerows(data)

print(f"IMDb movie data saved to {csv_filename}")

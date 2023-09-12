import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time

# Specify the path to the ChromeDriver executable
chromedriver_path = '/Users/srujithadevineni/web scrapping/chromedriver'

# Specify the folder for downloading PDFs
download_folder = '/Users/srujithadevineni/web scrapping/npl_pdfs'

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

# Create a new Chrome driver instance
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

url = "https://fid4sa-repository.ub.uni-heidelberg.de/view/schriftenreihen/sr-257.html?lang=en"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
whole_url = soup.find('div', class_="ep_view_page ep_view_page_view_schriftenreihen")

links_list = []
for link in whole_url.find_all('a', href=True):
    urls = link['href']
    links_list.append(urls)

for link in links_list:
    driver.get(link)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="firstContent"]/div/div/div[4]/table[1]/tbody/tr/td[2]/span/a[1]').click()

    # Wait until the file is downloaded completely
    time.sleep(1)
    while True:
        if any(fname.endswith('.crdownload') for fname in os.listdir(download_folder)):
            time.sleep(1)
        else:
            break

# Close the driver
driver.quit()

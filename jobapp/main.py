from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "clifftest33@gmail.com"
PASSWORD = "SuckMyDick"
website_url = ("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location="
               "London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
job_to_search = "Python Developer"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(website_url)

# Start SigningUp
time.sleep(4)
sign_button = driver.find_element(By.CSS_SELECTOR, ".nav__cta-container .nav__button-secondary")
sign_button.click()
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

# time.sleep(2)
# search_box = driver.find_element(By.XPATH, '//*[@id="keyword-typeahead-instance-ember101"]/div/label/svg[2]/use')
# search_box.clear()
# search_box.send_keys(job_to_search)
# search_box.send_keys(Keys.ENTER)
#
# time.sleep(2)
# easy_job = driver.find_element(By.XPATH, '//*[@id="ember105"]')
# easy_job.send_keys(Keys.ENTER)
time.sleep(5)
search_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
# all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for search in search_list:
    print("opening job")
    search.click()
    time.sleep(2)
    save_job = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
    save_job.click()

driver.quit()

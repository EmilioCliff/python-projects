from selenium import webdriver
from selenium.webdriver.common.by import By
import time
email = 'clifftest33@gmail.com'
password = 'ComeOnGuys'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://tinder.com/")
time.sleep(10)
# time.sleep(2)
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
login_button.click()

time.sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
# decline_button = driver.find_element(By.XPATH, '//*[@id="s1477815459"]/div/div[2]/div/div/div[1]/div[2]/button')
# decline_button.click()
# time.sleep(10)
# login_button = driver.find_element(By.XPATH, '//*[@id="s1477815459"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
# login_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
# login_button.click()
# time.sleep(10)
# use_facebook = driver.find_element(By.XPATH, '//*[@id="s-250565617"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
# use_facebook.click()
# use_facebook.click()
# email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
# email_input.send_keys(email)
# password_input = driver.find_element(By.XPATH, '')
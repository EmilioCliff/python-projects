from selenium import webdriver
from selenium.webdriver.common.by import By

wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=wikipedia_url)

article_number = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_number.text)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
speed_test = "https://www.speedtest.net/"
promised_up = 10
promised_down = 10


class InternetChecker:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.UP = 0
        self.DOWN = 0

    def get_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(20)
        ok_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        # ok_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        ok_button.click()
        sleep(180)
        self.UP = self.driver.find_element(By.CLASS_NAME, "download_speed")
        self.DOWN = self.driver.find_element(By.CLASS_NAME, "upload_speed")
        return [self.UP.text, self.DOWN.text]

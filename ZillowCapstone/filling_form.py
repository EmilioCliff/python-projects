from selenium import webdriver
from selenium.webdriver.common.by import By
import time

empty_form_url = "https://forms.gle/5oWuDBGPTW6q36c1A"
response_url = "https://docs.google.com/forms/d/1sgS-UYndbuEq3cBmnFlQ8odhnn5BQuSMHxlrB8RTTGw/edit#responses"


class FillData:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url=empty_form_url)
        time.sleep(3)

    def input_data(self, price, address, link):
        # self.driver.get(url=empty_form_url)
        # time.sleep(3)
        self.q1 = self.driver.find_element(By.XPATH,
                                           "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        self.q2 = self.driver.find_element(By.XPATH,
                                           "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        self.q3 = self.driver.find_element(By.XPATH,
                                           "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        self.submit_button = self.driver.find_element(By.XPATH,
                                                      "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")

        self.q1.send_keys(address)
        self.q2.send_keys(price)
        self.q3.send_keys(link)
        time.sleep(3)
        self.submit_button.click()
        time.sleep(3)
        # self.driver.quit()
        submit_another_response = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        submit_another_response.click()

#     def create_excel_file(self):
#         self.driver.get(url=response_url)
#         time.sleep(3)
#         handles = self.driver.window_handles
#         print(len(handles))
#         print(handles)
#         for handle in handles:
#             self.driver.switch_to.window(handle)
#         excel_link = self.driver.find_element(By.XPATH, "//*[@id='ResponsesView']/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]")
#         excel_link.click()
#         title_name = self.driver.find_element(By.XPATH, "//*[@id='yDmH0d']/div[14]/div/div[2]/span/div/div/span/div[1]/div/div/div[1]/div/div[1]/input")
#         title_name.send_keys("BnB's")
#         create_excel = self.driver.find_element(By.XPATH, "//*[@id='yDmH0d']/div[14]/div/div[2]/div[3]/div[2]/span/span")
#         create_excel.click()
#
#
# fill = FillData()
# fill.input_data("come", "on", "gunners")
# fill.create_excel_file()

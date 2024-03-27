from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from time import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
stop_time = time() + 60*1
while time() < stop_time:
    cookie = driver.find_element(By.ID, "cookie")
    end_time = time() + 10
    while time() < end_time:
        cookie.click()
    money_data = driver.find_element(By.ID, "money").text
    money = int("".join(money_data.split(",")))
    # print(money)
    store = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    purchase = {}
    for st in store:
        try:
            text = st.text.split("-")
            try:
                purchase[text[0]] = int("".join(text[-1].split(",")))
            except ValueError:
                continue
        except IndexError:
            continue
    # print(purchase)
    change = 0
    for (key, value) in purchase.items():
        if money > value:
            change = "".join(key.split())
    # print(change)
    clicker = driver.find_element(By.ID, f"buy{change}")
    clicker.click()
timer_sec = driver.find_element(By.ID, "cps").text
print(timer_sec)

# for pur in purchase:
#     print(pur.split()[-1])
# driver.get("http://secure-retreat-92358.herokuapp.com/")
# fName = driver.find_element(By.CLASS_NAME, "top")
# fName.send_keys("Cliff")
#
# lName = driver.find_element(By.CLASS_NAME, "middle")
# lName.send_keys("Emilio")
#
# email = driver.find_element(By.CLASS_NAME, "bottom")
# email.send_keys("clifflimo@gmail.com")
#
# send = driver.find_element(By.CLASS_NAME, "btn-block")
# send.send_keys(Keys.ENTER)


# driver.get("https://www.python.org/")
#
# time_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# title_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")
# events = {}
# for i in range(len(title_events)):
#     events[i] = {
#         "time": time_events[i].text,
#         "event": title_events[i].text
#     }
# print(events)

# driver.quit()

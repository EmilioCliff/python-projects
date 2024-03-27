from zillow_data import ZillowSoup
from filling_form import FillData
from time import sleep

zillow_data = ZillowSoup()
zillow_data.get_required_data()
fill = FillData()
for i in range(len(zillow_data.links)):
    sleep(3)
    fill.input_data(zillow_data.prices[i], zillow_data.addresses[i], zillow_data.links[i])

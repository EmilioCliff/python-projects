import csv
with open("cafe-data.csv", "r") as data:
    cafe_data = csv.reader(data)
    for cafe in cafe_data:
        print(cafe)
    # print(cafe_data)
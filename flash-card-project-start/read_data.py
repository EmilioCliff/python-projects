import pandas
import random
question_asked = []
df = pandas.read_csv("data/french_words.csv")
data_dict = df.to_dict()
data_list_french = [value for value in data_dict["French"].values()]
data_list_english = [value for value in data_dict["English"].values()]
random_number = random.randint(0, 103)
if random_number in question_asked:
    random_number = random.randint(0, 103)
question_asked.append(random_number)


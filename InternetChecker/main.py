from internetchecker import InternetChecker

twitter_bot = InternetChecker()
results = twitter_bot.get_speed()
print(results)

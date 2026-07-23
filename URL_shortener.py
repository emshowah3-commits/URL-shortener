import pyshorteners

# Users input of url
URL = input("Input a URL: ")

# shortner
shortener = pyshorteners.Shortener()

# Shortner the users url

short_URL = shortener.tinyurl.short(URL)
print(short_URL)
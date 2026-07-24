import pyshorteners


URL = input("Input a URL: ")

print("1. Short url")
print("2. Long url")
print("3. clean the Url")

option = int(input("Choose a url choose: "))

if option[1]:
    shortener = pyshorteners.Shortener()
    short_URL = shortener.tinyurl.short(URL)
    print("\n")
    print(short_URL)

elif option[2]:
    expanded_url = sl.tinyurl.expand(URL)
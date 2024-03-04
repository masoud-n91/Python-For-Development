import requests
import json

number = input("Which number do you like the most? ")
fruit = input("Which fruit do you like the most? ")


numberInfo = requests.get("http://numbersapi.com/" + number).text
fruitInfo = requests.get("https://www.fruityvice.com/api/fruit/" + fruit).text
spells = requests.get("https://hp-api.onrender.com/api/spells").text
advice = requests.get("https://api.adviceslip.com/advice").text


fruitJson = json.loads(fruitInfo)
spellsJson = json.loads(spells)
adviceJson = json.loads(advice)
adviceText = adviceJson.get("slip").get("advice")

print(f"About the number {number}:\n{numberInfo}")
print(f"About {fruit}:\n{fruitJson}")
print(f"My advice to you is:\n{adviceText}")
print(f"Here is the list of spells that you can use:\n{spells}")



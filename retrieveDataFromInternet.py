from urllib import request
import requests
import json
import pyttsx3

url = "http://official-joke-api.appspot.com/random_ten"

### Using python - request
# r = request.urlopen(url)
# data = r.read()
# jsonData = json.loads(data)
#
# print(r.getcode())
# print(jsonData)

### using requests
response = requests.get(url)
data2 = response.text
jsonData = json.loads(data2)
print(response.status_code)
print()

class Joke:

    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"Setup = {self.setup} - Punchline = {self.punchline}"


jokesList = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokesList.append(joke)

print(f"I got {len(jokesList)} jokes for you")

for joke in jokesList:
    print(joke)
    pyttsx3.speak("Setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("The Punchline")
    pyttsx3.speak(joke.punchline)
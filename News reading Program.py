import requests
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 125)
voices = engine.getProperty("voices")
engine.setProperty('voice', "english")


reqUrl = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=c42a725cfd5140aaba3d64b16885c0af'.format(apiKey="c42a725cfd5140aaba3d64b16885c0af")

headersList = {
 "Accept": "*/*",
}

response = requests.request("GET", reqUrl, headers=headersList)
data = response.json()
data = data["articles"]

engine.say("Starting the news")
engine.runAndWait()

articleNo = 1

for i in data:
  engine.say('article number {articleNo}'.format(articleNo=articleNo))
  engine.say(i["title"])
  print(i["title"])
  engine.runAndWait()
  articleNo += 1
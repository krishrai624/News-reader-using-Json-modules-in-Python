import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
print("This is the top headlines from TechCrunch.")
if __name__ == '__main__':
    speak("News from TechCrunch for Today. Please listen carefully")
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d5dd511c97da4404a747cf50e454f4fd"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("And here comes our next news for TOday....")
    speak("Thanks for listening...")

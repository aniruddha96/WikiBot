import requests
import json
from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York') 

class RasaHandler:
    
    def getRasaResponse(self,query):
        data = '{"text": "'+query+'","message_id" : "b2831e73-1407-4ba0-a861-0f30a42a2a5a"}'
        result = requests.post('http://localhost:5005/model/parse',data=data)
        j = result.json()
        resIntent = j['intent']['name']
        resConfience = j['intent']['confidence']
        print(resConfience)
        if(resConfience > 0.9):
            if resIntent == 'goodbye':
                return 'Good Bye!'
            if resIntent == 'deny':
                return 'Why do u diagree ?'
            if resIntent == 'mood_great':
                return 'I am happy for you'
            if resIntent == 'mood_unhappy':
                return 'dont be sad'
            if resIntent == 'bot_challenge':
                return 'Yes, I am a bot'
            if resIntent == 'react_positive':
                return 'yay'
            if resIntent == 'bye':
                return 'bye bye'
            if resIntent == 'canthelp':
                return 'Sorry, i was not helpful'
            if resIntent == 'explain':
                return 'My developers are still working on making me better'
            if resIntent == 'greet':
                return 'Hello !'
            if resIntent == 'thank':
                return 'Welcome come'
            if resIntent == 'ask_howbuilt':
                return 'I was build using Python, Solr, Rasa and BERT'
            if resIntent == 'ask_howdoing':
                return 'I am good'
            if resIntent == 'ask_howold':
                return 'I am 5 in bot years'
            if resIntent == 'ask_isbot':
                return 'Yes i am bot, my name is wikibot'
            if resIntent == 'ask_ishuman':
                return 'I am not a human'
            if resIntent == 'ask_time':
                datetime_NY = datetime.now(tz_NY)
                return "NY time: "+datetime_NY.strftime("%H:%M:%S")
            if resIntent == 'ask_weather':
                return 'Snowing in Buffalo'
            if resIntent == 'ask_whatisrasa':
                return 'Rasa is chatbot framework'
            if resIntent == 'ask_whatspossible':
                return 'I can chat with you using data scraped from reddit'
            if resIntent == 'ask_wherefrom':
                return 'Buffalo'
            if resIntent == 'ask_whoisit':
                return 'I am wikibot'
            
        else:
            return None
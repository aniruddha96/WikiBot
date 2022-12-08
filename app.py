from flask import Flask, request
from flask_cors import CORS
import requests
from ChitChatHandler import ChitChatHandler
from RedditDataHandler import RedditDataHandler
from RasaHandler import RasaHandler
import urllib.parse as urllib3
app = Flask(__name__)
CORS(app)

@app.route('/getresponse', methods=['GET'])
def search():
    args = request.args
    query = args.get("query", default="", type=str)
    core = args.get("core", default="default", type=str)
    searchPolitics = args.get("politics", default=0, type=int)
    searchEnvironment = args.get("environment", default=0, type=int)
    searchTechnology = args.get("technology", default=0, type=int)
    searchHealthcare = args.get("healthcare", default=0, type=int)
    searchEducation = args.get("education", default=0, type=int)
    searchAll = args.get("all", default=0, type=int)

    finalResponse = 'Sorry, I do not have an answer to this question.'
    #rasaResponse = rasa.getRasaResponse(query)
    #if  rasaResponse!= None:
    #    return rasaResponse

    if(cc.isChitChat(query)):
        chitChatResponse = cc.getChitChatResponse(query)
        if chitChatResponse == None:
            response = reddit.getResponse(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll)
            if response != None:
                finalResponse = response
        else:
            finalResponse = chitChatResponse
    else:
        response = reddit.getResponse(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll)
        if response != None:
            finalResponse = response
    return finalResponse

if __name__ == "__main__":
    cc = ChitChatHandler()
    reddit = RedditDataHandler()
    rasa = RasaHandler()
    app.run(host="0.0.0.0", port=9999)
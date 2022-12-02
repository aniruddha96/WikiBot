from flask import Flask, request
from flask_cors import CORS
import requests
from ChitChatHandler import ChitChatHandler

app = Flask(__name__)
CORS(app)

@app.route('/getresponse', methods=['GET'])
def search():
    args = request.args
    query = args.get("query", default="", type=str)
    core = args.get("core", default="default", type=str)
    searchPolitics = args.get("politics", default=False, type=bool)
    searchEnvironment = args.get("environment", default=False, type=bool)
    searchTechnology = args.get("technology", default=False, type=bool)
    searchHealthcare = args.get("healthcare", default=False, type=bool)
    searchEducation = args.get("education", default=False, type=bool)

    finalResponse = 'chatbot goes brrrrrrrrrrrrr'
    if(isChitChat(query)):
        chitChatResponse = getChitChatResponse(query)
        if chitChatResponse == None:
            response = getResponse(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation)
            if response != None:
                finalResponse = response
        else:
            finalResponse = chitChatResponse
    else:
        response = getResponse(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation)
        if response != None:
            finalResponse = response

    return finalResponse


def isChitChat(query):
    return False

def getChitChatResponse(query):
    return 'Dummy response'

def getResponse(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation):
    print('Searching '+ query +' on '+core+' core')
    print(searchPolitics)
    return 'Solr response'


if __name__ == "__main__":
    cc = ChitChatHandler()
    app.run(host="0.0.0.0", port=9999)
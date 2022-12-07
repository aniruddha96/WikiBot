from flask import Flask, request
from flask_cors import CORS
import requests
from ChitChatHandler import ChitChatHandler
from RedditDataHandler import RedditDataHandler
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

    finalResponse = 'chatbot goes brrrrrrrrrrrrr'
    if(cc.isChitChat(query)):
        chitChatResponse = getChitChatResponse(query)
        if chitChatResponse == None:
            response = getResponse(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll)
            if response != None:
                finalResponse = response
        else:
            finalResponse = chitChatResponse
    else:
        response = reddit.getResponse(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll)
        if response != None:
            finalResponse = response

    return finalResponse

def isChitChat(query):
    return False

def getChitChatResponse(query):
    return 'Dummy response'

def fq_formation(flag,type,filter_query):
    if flag and filter_query == '':
        filter_query += 'topic:' + type
    elif flag and filter_query != '':
        filter_query += ' OR topic:' + type
    return filter_query

def query_formation(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll):
    if searchAll:
        q_link = f'http://34.125.52.100:8983/solr/{core}/select?defType=edismax&df=parent_body&facet.field=topic&facet=true&fl=*%2Cscore&indent=true&q.op=OR&q={query}'
    else:
        filter_query = ''
        filter_query = fq_formation(searchPolitics,'Politics',filter_query)
        filter_query = fq_formation(searchEnvironment,'Environment',filter_query)
        filter_query = fq_formation(searchTechnology,'Technology',filter_query)
        filter_query = fq_formation(searchHealthcare,'Healthcare',filter_query)
        filter_query = fq_formation(searchEducation,'Education',filter_query)
        query = urllib3.quote(query)
        filter_query = urllib3.quote(filter_query)

        q_link = f'http://34.125.52.100:8983/solr/{core}/select?defType=edismax&df=parent_body&facet.field=topic&facet=true&fl=*%2Cscore&fq={filter_query}&indent=true&q.op=OR&q={query}'
    return q_link
    
def getResponse(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll):
    print('Searching '+ query +' on '+core+' core')
    
    q_link = query_formation(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll)
    print(q_link)
    return 'Solr response'

if __name__ == "__main__":
    cc = ChitChatHandler()
    reddit = RedditDataHandler()
    app.run(host="0.0.0.0", port=9999)
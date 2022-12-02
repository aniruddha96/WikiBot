from sentence_transformers import SentenceTransformer, util
import requests

class ChitChatHandler:
    
    def __init__(self):
        self.CORE_NAME = 'chitchat'
        self.solr_url = f'http://localhost:8983/solr/'
        self.model=model = SentenceTransformer('all-MiniLM-L6-v2')


    def searchFromSolr(self,query):
        result = requests.get('http://localhost:8983/solr/chitchat/select?indent=true&q.op=OR&q=input%3A'+query+'&rows=100')
        return result
    
    def nlpFilter(self,result,query):
        qembeddings = self.model.encode(query, convert_to_tensor=True)
        response = None
        score = None
        matchedBest =None
        for doc in result.json()['response']['docs']:
            inp = doc['input'][0]
            inpemb= self.model.encode(inp, convert_to_tensor=True)
            cosine_score = util.cos_sim(inpemb, qembeddings)
            if score == None or cosine_score > score:
                score = cosine_score
                matchedBest = inp
                response = doc['response'][0]

        print('query : '+query)
        print('Just Solr match : '+ result.json()['response']['docs'][0]['input'][0])
        print('Embedding match : '+ matchedBest)
        print('Response : '+response)
        return response

    def selectTop(self,result):
        return result.json()['response']['docs'][0]['input'][0]

    def isChitChat(self,query):
        return False

    def getChitChatResponse(self,query):
        return 'Dummy response'
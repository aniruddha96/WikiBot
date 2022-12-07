from sentence_transformers import SentenceTransformer, util
import requests
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from tensorflow.keras.models import model_from_json

class ChitChatHandler:
    
    def __init__(self):
        self.CORE_NAME = 'chitchat'
        self.solr_url = f'http://localhost:8983/solr/'
        self.model=model = SentenceTransformer('all-MiniLM-L6-v2')

        json_file = open('model_new.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()

        self.loaded_model = model_from_json(loaded_model_json, custom_objects={'KerasLayer':hub.KerasLayer})
        # load weights into new model
        self.loaded_model.load_weights("model_new.h5")


    def searchFromSolr(self,query):
        result = requests.get('http://localhost:8983/solr/chitchat/select?indent=true&q.op=OR&q=input%3A'+query+'&rows=100')
        return self.nlpFilter(result,query)
    
    def nlpFilter(self,result,query):
        qembeddings = self.model.encode(query, convert_to_tensor=True)
        response = None
        score = None
        matchedBest =None
        for doc in result.json()['response']['docs']:
            inp = doc['input']
            inpemb= self.model.encode(inp, convert_to_tensor=True)
            cosine_score = util.cos_sim(inpemb, qembeddings)
            if score == None or cosine_score > score:
                score = cosine_score
                matchedBest = inp
                response = doc['response']

        print('query : '+query)
        print('Just Solr match : '+ result.json()['response']['docs'][0]['input'])
        print('Embedding match : '+ matchedBest)
        print('Response : '+response)
        return response

    def selectTop(self,result):
        return result.json()['response']['docs'][0]['input']

    def isChitChat(self,query):
        prediction = self.loaded_model.predict([query])
        if prediction <= 0.3:
            return True
        return False

    def getChitChatResponse(self,query):
        return 'Dummy response'
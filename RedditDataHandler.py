from sentence_transformers import SentenceTransformer, util
import requests

class RedditDataHandler:

    def __init__(self):
        self.solr_url = f'http://localhost:8983/solr/'
        self.model=model = SentenceTransformer('all-MiniLM-L6-v2')

    def getResponse(self,query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation):
        print('Searching '+ query +' on '+core+' core')
        print(searchPolitics)
        return 'Solr response'

    def querySolr(self,query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation):
        result = requests.get('http://localhost:8983/solr/IRF22P1/select?indent=true&q.op=OR&q=parent_body%3A'+query+'&rows=100')
        return result

    def nlpFilter(self,result,query):
        qembeddings = self.model.encode(query, convert_to_tensor=True)
        result = requests.get('http://localhost:8983/solr/IRF22P1/select?indent=true&q.op=OR&q=parent_body%3A'+query+'&rows=100')
        response = None
        score = None
        matchedBest =None
        for doc in result.json()['response']['docs']:
            inp = doc['parent_body']
            inpemb= self.model.encode(inp, convert_to_tensor=True)
            cosine_score = util.cos_sim(inpemb, qembeddings)
            if score == None or cosine_score > score:
                score = cosine_score
                matchedBest = inp
                response = doc['body']

        print('query : '+query)
        print('Just Solr match : '+ result.json()['response']['docs'][0]['parent_body'])
        print('Embedding match : '+ matchedBest)
        print('Response : '+response)

        return response

    def selectTop(self,result):
        return result.json()['response']['docs'][0]['parent_body']
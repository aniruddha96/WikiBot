from sentence_transformers import SentenceTransformer, util
import requests
import urllib.parse as urllib3

class Matches:
    def __init__(self):
        self.responses = []
        self.text=None
        self.solrScore=0
        self.embScore=0
        self.id=None
       
    def __repr__(self):
        return str(self.text)+'  '+str(self.solrScore)+'  '+str(self.embScore)
    
    def to_dict(self,alpha,beta):
        return {
            'id':self.id,
            'string': self.text,
            'weighted solr score':self.solrScore*alpha,
            'weighted emb score':self.embScore*beta
        }

class RedditDataHandler:

    def __init__(self):
        self.solr_url = f'http://localhost:8983/solr/'
        self.model=model = SentenceTransformer('all-MiniLM-L6-v2')

    def fq_formation(self,flag,type,filter_query):
        if flag and filter_query == '':
            filter_query += 'topic:' + type
        elif flag and filter_query != '':
            filter_query += ' OR topic:' + type
        return filter_query

    def query_formation(self,query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll):
        if searchAll:
            q_link = f'http://34.125.52.100:8983/solr/{core}/select?defType=edismax&df=parent_body&facet.field=topic&facet=true&fl=*%2Cscore&indent=true&q.op=OR&q={query}'
        else:
            filter_query = ''
            filter_query = self.fq_formation(searchPolitics,'Politics',filter_query)
            filter_query = self.fq_formation(searchEnvironment,'Environment',filter_query)
            filter_query = self.fq_formation(searchTechnology,'Technology',filter_query)
            filter_query = self.fq_formation(searchHealthcare,'Healthcare',filter_query)
            filter_query = self.fq_formation(searchEducation,'Education',filter_query)
            query = urllib3.quote(query)
            filter_query = urllib3.quote(filter_query)

            q_link = f'http://34.125.52.100:8983/solr/{core}/select?defType=edismax&df=parent_body&facet.field=topic&facet=true&fl=*%2Cscore&fq={filter_query}&indent=true&q.op=OR&q={query}'
        return q_link
        
    def getResponse(self,query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll):
        print('Searching '+ query +' on '+core+' core')
        
        q_link = self.query_formation(query,core,searchPolitics,searchEnvironment,searchTechnology,searchHealthcare,searchEducation,searchAll)
        result = requests.get(q_link)
        print(q_link)
        topResult = self.nlpFilter(result,query)
        
        return result
    
    def getMostUpVotedResponse(self,match):
        res = None
        upvotes = None
        for pair in match.responses:
            if upvotes == None or pair[1] > upvotes :
                res = pair[0]
                upvotes = pair[1]
        
        return res
        
    def nlpFilter(self,result,query):
        qembeddings = self.model.encode(query, convert_to_tensor=True)
        res = {}
        for doc in result.json()['response']['docs']:
            inp = doc['parent_body']
            inpemb= self.model.encode(inp, convert_to_tensor=True)
            cosine_score = util.cos_sim(inpemb, qembeddings)
            match = None
            if inp in res:
                match = res[inp]
                match.responses.append((doc['body'],doc['upvotes']))
            else:
                match = Matches()
                match.solrScore = doc['score']
                match.embScore = float(cosine_score[0])
                match.responses.append((doc['body'],doc['upvotes']))
                match.text = inp
                match.id = doc['id']
                res[inp]=match
        
        def getBestMatchResponse(alpha,beta):
            alpha = 1
            beta = 2

            def comparator(a):
                return alpha*a.solrScore + beta*a.embScore
        
            mat = list(res.values())
            mat.sort(key=comparator)
        
            return mat[0]
        
        
        return getBestMatchResponse(1,3)
    
    
    def getMatchesList(self,result,query):
        qembeddings = self.model.encode(query, convert_to_tensor=True)
        res = {}
        for doc in result.json()['response']['docs']:
            inp = doc['parent_body']
            inpemb= self.model.encode(inp, convert_to_tensor=True)
            cosine_score = util.cos_sim(inpemb, qembeddings)
            match = None
            if inp in res:
                match = res[inp]
                match.responses.append((doc['body'],doc['upvotes']))
            else:
                match = Matches()
                match.solrScore = doc['score']
                match.embScore = float(cosine_score[0])
                match.responses.append((doc['body'],doc['upvotes']))
                match.text = inp
                match.id = doc['id']
                res[inp]=match

        return res
        
    def selectTop(self,result):
        return result.json()['response']['docs'][0]['parent_body']
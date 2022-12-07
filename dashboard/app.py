import streamlit as st
from RedditDataHandler import RedditDataHandler
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import numpy
import pandas as pd

query = st.sidebar.text_input('Input','')
Technology = st.sidebar.checkbox('Technology')
Politics = st.sidebar.checkbox('Politics')
Environment = st.sidebar.checkbox('Environment')
Healthcare = st.sidebar.checkbox('Healthcare')
Education = st.sidebar.checkbox('Education',disabled=False)
All = st.sidebar.checkbox('All')

alpha = st.sidebar.number_input('Alpha')
beta = st.sidebar.number_input('beta')


 
# Random Data
random_x = [100, 2000, 550]
names = ['A', 'B', 'C']
 
fig2 = px.pie(values=random_x, names=names)


redd = RedditDataHandler()

def renderTotalResPieChart(j):
    topic=True
    topics= []
    counts= []
    for i in j['facet_counts']['facet_fields']['topic']:
        if topic:
            topics.append(i)
            topic=False
        else:
            counts.append(i)

    fig = px.pie(values=counts, names=topics)
    st.plotly_chart(fig, use_container_width=True)

def matchesToDF(matches):
    df = pd.DataFrame.from_records([s.to_dict(1,1) for s in matches])
    return df

def renderBarGraph(res,query):
    l = redd.getMatchesList(res,query)
    df = matchesToDF(l.values())
    fig = px.bar(df, x="id", y=["weighted solr score", "weighted emb score"], title="Scoring matches",hover_data=['string'])
    st.plotly_chart(fig, use_container_width=True)

def render():
    expander = st.expander("Solr Result")
    resultJson = redd.getResponse(query,'reddit',True,True,True,True,True,True)
    j = resultJson.json()
    expander.write(j)
    renderTotalResPieChart(j)
    renderBarGraph(resultJson,query)

    matches = redd.getMatchesList(resultJson,query)
    
    
if st.sidebar.button('Submit'):
    render()



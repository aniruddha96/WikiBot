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
            topic=True
    print(topics)
    fig = px.pie(values=counts, names=topics,title='Distribution of matches by topic')
    st.plotly_chart(fig, use_container_width=True)

def matchesToDF(matches):
    df = pd.DataFrame.from_records([s.to_dict(1,1) for s in matches])
    return df

def matchToDF(match):
    df = pd.DataFrame(match.responses, columns =['Response', 'Upvotes'])
    return df

def renderBarGraph(res,query):
    l = redd.getMatchesList(res,query)
    df = matchesToDF(l.values())
    fig = px.bar(df, x="id", y=["weighted solr score", "weighted emb score"], title="Scoring matches",hover_data=['string'])
    st.plotly_chart(fig, use_container_width=True)

def renderResponsesBarGraph(res,query):
    topResponse=  redd.nlpFilter(res,query)
    df = matchToDF(topResponse)
    print(df)
    fig = px.bar(df,x = "Response", y=["Upvotes"], title="Response and Upvotes ",hover_data=['Response'])
    st.plotly_chart(fig, use_container_width=True)

def render():
    expander = st.expander("Expand to see raw solr response")
    resultJson = redd.getResponse(query,'reddit',True,True,True,True,True,1)
    j = resultJson.json()
    expander.write(j)
    renderTotalResPieChart(j)
    renderBarGraph(resultJson,query)
    renderResponsesBarGraph(resultJson,query)
    
    
if st.sidebar.button('Submit'):
    render()



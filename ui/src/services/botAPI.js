import axios from 'axios';

export const api = 'http://34.125.52.100:9999'

export const getChatbotResponse = (query, topics) =>
  axios.get(`${api}/getresponse?query=${query}&politics=${topics.politics}&environment=${topics.environment}&technology=${topics.technology}&healthcare=${topics.healthcare}&education=${topics.education}&all=${topics.all}&core=reddit`)

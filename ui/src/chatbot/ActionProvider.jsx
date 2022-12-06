// in ActionProvider.jsx
import React from 'react';
import { useSelector } from 'react-redux'
import { getChatbotResponse } from '../services/botAPI'

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const handleHello = () => {
    const botMessage = createChatBotMessage('Hello. Nice to meet you.');

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));

  };

  const selectedTopics = useSelector((state) => state.topics.selectedTopics)

  const handleInput = async (query) => {

    let topics = {
      politics: false,
      technology: false,
      education: false,
      environment: false,
      healthcare: false,
      all: false,
    }
    for (var selectedTopic of selectedTopics) {
      console.log(selectedTopic);
      topics[selectedTopic] = true
    }
    const res = await getChatbotResponse(query, topics)
                  .then((response) => {return response.data})
    const botMessage = createChatBotMessage(res);

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));

  };
  // Put the handleHello function in the actions object to pass to the MessageParser
  return (
    <div>
    {
      React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleHello,
            handleInput,
          },
        });
      })
    }
    </div>
  );
};

export default ActionProvider;
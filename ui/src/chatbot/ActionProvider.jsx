// in ActionProvider.jsx
import React from 'react';

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const handleHello = () => {
    const botMessage = createChatBotMessage('Hello. Nice to meet you.');

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));

  };

  const handleInput = async (query) => {
    const res = await fetch('http://127.0.0.1:9999/getresponse?query='+query+'&politics=true&environment=true&technology=true&healthcare=true&education=true&core=default')
      .then((response) => {return response.text()});
    console.log(res)
    const botMessage = createChatBotMessage(res);

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));

  };
  // Put the handleHello function in the actions object to pass to the MessageParser
  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleHello,
            handleInput,
          },
        });
      })}
    </div>
  );
};

export default ActionProvider;
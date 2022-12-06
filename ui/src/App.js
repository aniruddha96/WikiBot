import React from "react";
import Chatbot from "react-chatbot-kit";
import Topics from './checkbox/Topics';
import 'react-chatbot-kit/build/main.css'
import config from "./configs/chatbotConfig";
import MessageParser from "./chatbot/MessageParser";
import ActionProvider from "./chatbot/ActionProvider";
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';

function App() {
  return (
    <div className="App">
      <Grid container direction="row" alignItems="center">
        <Chatbot
          config={config}
          messageParser={MessageParser}
          actionProvider={ActionProvider}
        />
        <Topics/>
      </Grid>
    </div>
  );
}

export default App;
import React from "react";
import Chatbot from "react-chatbot-kit";
import Topics from './checkbox/Topics';
import 'react-chatbot-kit/build/main.css'
import config from "./configs/chatbotConfig";
import MessageParser from "./chatbot/MessageParser";
import ActionProvider from "./chatbot/ActionProvider";
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import background from "./gradient.png"
import "./App.css"

function App() {

    const myStyle={
      backgroundImage: `url(${background})`,
      height:'100vh',
      // marginTop:'-70px',
      // fontSize:'50px',
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
    };
    return (
      <div style={myStyle}>
        <div className="App">
          <Grid container direction="row" alignItems="center" height="100vh" justifyContent="center">
            <Chatbot
              config={config}
              messageParser={MessageParser}
              actionProvider={ActionProvider}
            />
            <Topics/>
          </Grid>
        </div>
      </div>
    );
  
}

export default App;
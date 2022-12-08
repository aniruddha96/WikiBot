import React from "react";
import Chatbot from "react-chatbot-kit";
import Topics from './checkbox/Topics';
import 'react-chatbot-kit/build/main.css'
import config from "./configs/chatbotConfig";
import MessageParser from "./chatbot/MessageParser";
import ActionProvider from "./chatbot/ActionProvider";
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import background from "./gradient.png"
import "./App.css"

function App() {
  const myStyle={
    backgroundImage: `url(${background})`,
    height:'100%',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
  };
  const routeChange = () =>{
    window.location.href = `http://34.125.34.68:8501/`
  }
  return (
    <div style={myStyle}>
      <div className="App">
        <Grid direction="column" alignItems="center">
          <Grid container direction="row" alignItems="center" height="100vh" justifyContent="center">
            <Chatbot
              config={config}
              messageParser={MessageParser}
              actionProvider={ActionProvider}
            />
            <Topics/>
            <Button size="large" variant="contained" onClick={routeChange}>Take me to debug visualisation.</Button>
          </Grid>

        </Grid>
      </div>
    </div>
  );
}

export default App;
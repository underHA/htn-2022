import { useState } from 'react';
import './App.css';
import Home from "./home/Home.js"
import Watch from "./watch/Watch.js"
import { siteContext } from "./Context.js"
import MockCards from "./watch/MockCards";

function App() {
  const [page, setPage] = useState("home")
  const [settings, setSettings] = useState({ closedCaptioning: true })

  const caption = "This is, what we in the industry call a certified hood classic. This however, is lorem ipsum dolor sit amet is placeholder text"

  return (
    <siteContext.Provider value={{page, setPage, settings, setSettings}}>
      <div className="App">
        {page == "loading"? <></> : (page == "home"? <Home />:<Watch historyCards={MockCards} caption={caption} />)}
      </div>
    </siteContext.Provider>
  );
}

export default App;

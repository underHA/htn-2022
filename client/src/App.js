import { useState } from 'react';
import './App.css';
import Home from "./home/Home.js"
import Watch from "./watch/Watch.js"
import { siteContext } from "./Context.js"

function App() {
  const [page, setPage] = useState("home")
  const [settings, setSettings] = useState({ closedCaptioning: true })

  return (
    <siteContext.Provider value={{page, setPage, settings, setSettings}}>
      <div className="App">
        {page == "loading"? <></> : (page == "home"? <Home />:<Watch />)}
      </div>
    </siteContext.Provider>
  );
}

export default App;

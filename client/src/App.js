import { useState } from 'react';
import './App.css';
import Home from "./home/Home.js"
import Watch from "./watch/Watch.js"
import Loading from "./loading/Loading.js"
import { siteContext } from "./Context.js"
import axios from "axios";

function App() {
  const [page, setPage] = useState("home")
  const [settings, setSettings] = useState({ closedCaptioning: true })
  const [data, setData] = useState([])
  const [music, setMusic] = useState(false)

  const requestVideoAudio = (entireText, styleType) => {
    setPage("loading")
    const styleString = styleLib[styleType || Object.keys(styleLib)[0]]
    console.log("hello")

    // Request the video generation
    axios.post('http://localhost:5000/api/get_video', {
          text: entireText,
          style: styleString
      })
      .then(response => {
        setData(response.data)
        setPage("watch")
        console.log("hello")
      })
      .catch(error => {
          console.log(error);
      });

    // Request the background music
    axios.post('http://localhost:5000/api/get_music', {
          text: entireText
      })
      .then(response => {setMusic(response.data)})
      .catch(error => {
          console.log(error)
      })
  }

  return (
    <siteContext.Provider value={{page, setPage, settings, setSettings, data, setData, music, setMusic, requestVideoAudio}}>
      <div className="App">
        {page == "loading"? <Loading /> : (page == "home"? <Home />:<Watch />)}
      </div>
    </siteContext.Provider>
  );
}

export const styleLib = {
  photorealistic: "(insert prompt),muscle extremely detailed, face, trending on artstation, pixiv, cgsociety, hyperdetailed Unreal Engine, optimization 4k 8k ultra HD, WLOP",
  surrealist: "(insert prompt) by greg rutkowski, ultradetailed digital painting, 8 k, realism, intriguing",
  pastel: "(insert prompt), depressed mood, in the style of artgerm, gerald brom, atey ghailan and mike mignola, vibrant colors and hard shadows and strong rim light, plain background, comic cover art, trending on artstation",
  psychedelic: "a painting of many synthwave colors and (insert prompt), an ultrafine detailed painting by unkoku togan, pixiv contest winner, space art, cosmic horror, lovecraftian, psychedelic ",
  cinematic: "realistic screenshot from blade runner movie of (insert prompt) intricate, moody lighting, highly detailed, cinematic, photoreal octane rendering, denis villeneuve, craig mullins, ridley scott ",
  dreamy: "(insert prompt), trending on Artstation, painting by Jules Julien, Leslie David and Lisa Frank and Peter Mohrbacher and Alena Aenami and Dave LaChapelle muted colors with minimalism",
  fable: "(insert prompt) in the Style of Atey Ghailan and Mike Mignola and Artgerm, vibrant colors, hard shadows,  Comic Cover Art, trending on artstation",
  anime: "soft studio lighting delicate features finely detailed (insert prompt), trending on pixiv fanbox, illustrated by greg rutkowski makoto shinkai takashi takeuchi studio ghibli",
  cartoon: "(insert prompt), graduation album cover color palette : : by martine johanna and simon stalenhag and chie yoshii and casey weldon and wlop : : ornate, dynamic, particulate, rich colors, intricate, elegant, highly detailed, vogue, harper's bazaar art, fashion magazine, smooth, sharp focus, 8 k, octane render, "
}

export default App;

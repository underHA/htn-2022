import React, { useContext, useRef, useState } from "react"
import "./Home.css"
import { BsFillCloudMoonFill, BsArrowRight } from "react-icons/bs"
import Dropdown from "../common/Dropdown"
import TextField from "../common/TextField"
import { siteContext } from "../Context"
import backdrop from "./backdrop.png"
import { styleLib } from "../App"

const Home = (props) => {
    const {page, setPage} = useContext(siteContext)
    const {data, setData} = useContext(siteContext)
    const {music, setMusic} = useContext(siteContext)
    const [style, setStyle] = useState(Object.keys(styleLib)[0])
    const {requestVideoAudio} = useContext(siteContext)
    const textRef = useRef();

    const handleGenerate = (e) => {
        if (textRef.current) {
            requestVideoAudio(textRef.current.value, style)
        }
    }


    return (
        <div className="home-container">
            <img className="background-image" alt="" src={backdrop} style={{width: "100%"}}/>
            <div className="left-UI">
                <div className="header-container">
                    <BsFillCloudMoonFill size={32} className="header-icon"/>
                    <div>
                        <p className="header-big">Lucid.ai</p>
                        <p className="header-small">Your favourite text as a movie, directed by AI.</p>
                    </div>
                </div>

                <textarea ref={textRef} className="story-input" type="text" placeholder="Tell me a story..."></textarea>
            </div>

            <div className="right-UI">
                <div className="question-container">
                    <p className="question-heading">Video Art Style</p>
                    <Dropdown options={Object.keys(styleLib)} setStyle={setStyle}/>
                </div>

                <div className="question-container">
                    <p className="question-heading">Add Video Attributes</p>
                    <TextField/>
                </div>

                <div className="generate-container" onClick={handleGenerate}>
                    <BsArrowRight size={18} fill={"#FFFFFF"}/>
                    <p className="generate-text">Generate!</p>
                </div>
            </div>
        </div>
    )
}

export default Home
import React, { useContext } from "react"
import "./Home.css"
import { BsFillCloudMoonFill, BsArrowRight } from "react-icons/bs"
import Dropdown from "../common/Dropdown"
import TextField from "../common/TextField"
import { siteContext } from "../Context"

const Home = (props) => {
    const {page, setPage} = useContext(siteContext)

    return (
        <div className="home-container">
            <img className="background-image" alt="" src="https://static01.nyt.com/images/2022/09/01/business/00roose-1/merlin_212276709_3104aef5-3dc4-4288-bb44-9e5624db0b37-superJumbo.jpg"/>
            {/* <iframe title="bruh" width={100} height={100} src={`${"https://www.youtube.com/watch?v=r-mAyu5RruU"}?autoplay=1`}></iframe> */}
            {/* <iframe width="200" height="100" src={`${"https://www.youtube.com/embed/r-mAyu5RruU"}?autoplay=1`} frameborder="0" allow="autoplay;" allowfullscreen></iframe> */}
            <div className="left-UI">
                <div className="header-container">
                    <BsFillCloudMoonFill size={32} className="header-icon"/>
                    <div>
                        <p className="header-big">Lucid.ai</p>
                        <p className="header-small">Book to Movie</p>
                    </div>
                </div>

                <textarea className="story-input" type="text" placeholder="Tell me a story..."></textarea>
            </div>

            <div className="right-UI">
                <div className="question-container">
                    <p className="question-heading">Video Art Style</p>
                    <Dropdown options={["Photorealistic", "Surrealist", "Pokemon", "Spongebob"]}/>
                </div>

                <div className="question-container">
                    <p className="question-heading">Add Video Attributes</p>
                    <TextField/>
                </div>

                <div className="generate-container" onClick={() => {setPage("watch")}}>
                    <BsArrowRight size={18} fill={"#FFFFFF"}/>
                    <p className="generate-text">Generate!</p>
                </div>
            </div>
        </div>
    )
}

export default Home
import React, { useContext, useEffect, useRef } from "react";
import "./Watch.css"
import { siteContext } from "../Context";
import HistoryBar from "./HistoryBar";
import { BsFullscreen } from "react-icons/bs";

const Watch = ({ historyCards, caption }) => {
    const { settings, setSettings } = useContext(siteContext)
    const videoRef = useRef()

    useEffect(() => {
        if (videoRef.current) {
            const video = videoRef.current
            /* play video twice as fast */
            video.defaultPlaybackRate = 0.5;
            video.play();
    
            // /* now play three times as fast just for the heck of it */
            video.playbackRate = 3.0;
        }
    })

    return (
        <div className="watch-container">
            <HistoryBar historyCards={historyCards}/>

            <div className="content-container">
                <div className="fullscreen-button">
                    <BsFullscreen size={24} fill={"#FFFFFF"} />
                </div>
                <video ref={videoRef} style={{ display: "flex", flexGrow: 1 }} controls loop>
                    <source src="https://htn-bucket.s3.us-east-2.amazonaws.com/20220917022903%20(1).mp4" type="video/mp4"/>
                    {/* <source src="movie.ogg" type="video/ogg"/> */}
                </video>
                {/* <img className="video" src={"https://external-preview.redd.it/6Ijx9IWBYX_bgmsHoXWUw5ycowCKkuqcULHCOynXGWM.jpg?auto=webp&s=4bdd6f097e1592d7033eee41d88dbebb6acaad2a"} /> */}
                
                {settings.closedCaptioning? (
                    <p className="closed-captioning">{caption}</p>
                ) : <></>}
            </div>
        </div>
    )
}

export default Watch
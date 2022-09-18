import React, { useContext, useEffect, useRef, useState } from "react";
import "./Watch.css"
import { siteContext } from "../Context";
import HistoryBar from "./HistoryBar";
import { BsFullscreen } from "react-icons/bs";
import readme from "./readme.mp3"

const Watch = ({ }) => {
    const { settings, data, music } = useContext(siteContext)
    const [playing, setPlaying] = useState(0)
    const [currVid, setCurrVid] = useState();
    const [currAud, setCurrAud] = useState();
    const [musicVid, setMusicVid] = useState();
    const videoRef = useRef()
    const audioRef = useRef()
    const musicRef = useRef()

    // useEffect(() => {
    //     if (videoRef.current) {
    //         const video = videoRef.current
    //         video.defaultPlaybackRate = 0.5;
    //         video.play();
    //         video.playbackRate = 0.5;
    //     }
    // }, [])

    const handleAudioEnd = () => {
        setPlaying(Math.min(playing + 1, Math.max(0, data.length - 1)))
    }

    useEffect(() => {
        console.log(data[playing].video, data[playing].audio)

        setCurrVid(
            <video key={data[playing].video} ref={videoRef} style={{ display: "flex", flexGrow: 1 }} loop>
                <source src={data[playing].video[1]} type="video/mp4"/>
            </video>
        )

        setCurrAud(
            <audio key={data[playing].audio} ref={audioRef} style={{ display: "none" }} onEnded={handleAudioEnd}>
                <source src={data[playing].audio[1]} type="audio/wav"></source>
            </audio>
        )

    }, [playing])

    useEffect(() => {
        if (videoRef.current) {
            videoRef.current.play();
        }
    }, [currVid])

    useEffect(() => {
        if (audioRef.current) {
            audioRef.current.play();
        }
    }, [currAud])

    useEffect(() => {
        setMusicVid(
            <audio key={data[playing].audio} ref={musicRef} volume={0.5} style={{ display: "none" }} onEnded={handleAudioEnd} autoPlay loop>
                <source src={readme} type="audio/wav"></source>
            </audio>
            // <iframe width="560" height="315" src={`${music}`} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        )
    }, [music])

    return (
        <div className="watch-container">
            <HistoryBar playing={playing}/>

            <div className="content-container">
                <div className="fullscreen-button">
                    <BsFullscreen size={24} fill={"#FFFFFF"} />
                </div>

                <div id="player"></div>

                {musicVid}
                {currVid}
                {currAud}

                {settings.closedCaptioning && data[playing].chunk !== ""? (
                    <p className="closed-captioning">{data[playing].chunk}</p>
                ) : <></>}
            </div>
        </div>
    )
}

export default Watch
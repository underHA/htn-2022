import React, { useContext, useEffect, useState } from "react"
import { FaClosedCaptioning } from "react-icons/fa"
import { siteContext } from "../Context"
import "./HistoryBar.css"

const HistoryBar = () => {
    const { settings, setSettings, data } = useContext(siteContext)
    const [cardRenders, setCardRenders] = useState([])

    useEffect(() => {
        const newCards = data.map(item => {
            return (
                <div className="historycard-container">
                    <p className="historycard-text">{item.chunk}</p>
                    <img className="historycard-image" alt="" src={item.thumbnail}/>
                </div>
            )
        })

        setCardRenders(newCards)
    }, [data])

    return (
        <div className="history-container">
            <div className="history-top">
                {cardRenders}
            </div>

            <div className="history-bottom">
                <div className="controls-texts">
                    <p className="controls-heading">Lucid.ai</p>
                    <p className="controls-subheading">v 1.0.0</p>
                </div>
                <div className="btt-closedcaptions" style={{backgroundColor: settings.closedCaptioning? "#":""}} onClick={() => {setSettings(prev => ({...prev, closedCaptioning: !prev.closedCaptioning}))}}>
                    <FaClosedCaptioning size={24} fill={settings.closedCaptioning? "#FFFFFF":"#555555"}/>
                </div>
            </div>
        </div>
    )
}

export default HistoryBar
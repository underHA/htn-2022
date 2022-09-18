import React, { useContext } from "react";
import "./Watch.css"
import { siteContext } from "../Context";
import HistoryBar from "./HistoryBar";
import MockCards from "./MockCards";

const Watch = ({ historyCards }) => {
    const { settings, setSettings } = useContext(siteContext)

    return (
        <div className="watch-container">
            <HistoryBar historyCards={MockCards}/>
            <div className="content-container">
                
            </div>
        </div>
    )
}

export default Watch
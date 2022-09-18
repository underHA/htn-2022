import React, { useEffect, useState } from "react"
import { GoTriangleDown } from "react-icons/go"
import "./Dropdown.css"

const Dropdown = ({options}) => {
    const [value, setValue] = useState(); // Stores the index of the item in options
    const [dropVisible, setDropVisible] = useState(false);
    const [dropRender, setDropRender] = useState();

    let optionRenders = [];
    for (let i=0; i<options.length; i++) {
        let sortedOptions = options.sort((a, b) => a.localeCompare(b));
        let option = sortedOptions[i];
        optionRenders.push(
            <div className="dropdown-option-container" onClick={() => {
                setDropVisible(!dropVisible);
                setValue(i);
                }}>
                <div className="dropdown-text-container">
                    <p className="nowrap">{option}</p>
                </div>
            </div>
        )
    }

    useEffect(() => {
        if (dropVisible) {
            setDropRender(
                <div className="dropdown-field">
                    {optionRenders}
                </div>
            );
        } else {
            setDropRender(<></>);
        }
    }, [dropVisible])

    return (
        <div className={dropVisible? "dropdown-bar super-z":"dropdown-bar"} onClick={() => setDropVisible(!dropVisible)}>
            <div className={dropVisible? "dropdown-defocuser":"hidden"} onClick={() => setDropVisible(false)}></div>
            <div className="dropdown-text-container">
                <p className="dropdown-selection-text">{options[value]}</p>
            </div>
            <GoTriangleDown size={10} className="dropdown-triangle"/>
            {dropRender}
        </div>
    )
}

export default Dropdown
import { useState } from 'react'
import {
    CCard, 
    CCardImage, 
    CCardBody, 
    CCardTitle, 
    CCardText, 
    CCardGroup,
} from '@coreui/react'

import './Form.css';

const Form = () => {
    const [checked, setChecked] = useState({
        "Action": false,
        "Racing / Driving": false,
        "Strategy": false,
        "Sports": false,
        "Simulation": false,
        "Adventure": false,
        "Role-Playing (RPG)": false,
        "Educational": false,
    })
    const [priceRange, setPriceRange] = useState([0, 60])
    const [timeRange, setTimeRange] = useState([0, 40])
    const [online, setOnline] = useState(2)

    const [submitted, setSubmitted] = useState(false)
    const [data, setData] = useState([{}])

    const toggleChecked = (genre) => {
        setChecked({...checked, [genre]: !checked[genre]})
    }

    const editPriceRange = (pos, val) => {
        console.log()
        let newArr = [...priceRange]
        if(val === "")
            newArr[pos] = (pos === 0)? 0 : 99
        else
            newArr[pos] = parseInt(val)
        setPriceRange(newArr)
    }

    const editTimeRange = (pos, val) => {
        let newArr = [...timeRange]
        if(val === "")
            newArr[pos] = (pos === 0)? 0 : 999
        else
            newArr[pos] = parseInt(val)
        setTimeRange(newArr)
    }

    const resetState = () => {
        setChecked({
            "Action": false,
            "Racing / Driving": false,
            "Strategy": false,
            "Sports": false,
            "Simulation": false,
            "Adventure": false,
            "Role-Playing (RPG)": false,
            "Educational": false,
        })
        setPriceRange([0, 60])
        setTimeRange([0, 40])
        setOnline(2)
    }

    const selectedButton = {
        backgroundColor: "#34aeeb",
        color: "white"
    }

    const nonSelectedButton = {
        backgroundColor: "white"
    }

    const submitHandler = async (method) => {
        try {
            // Convert checked boxes as a list of genres
            const genres = []
            Object.entries(checked).forEach(([key, value]) => {
                if(value === true) genres.push(key)
            })
            // Set up payload
            const payload = {
                genres: genres,
                priceRange: priceRange,
                timeRange: timeRange,
                online: online,
            }
            // Request recommendations
            const req = await fetch(`http://127.0.0.1:8000/${method}`, {
                method: "POST",
                header: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            })
            // Response as 15 returned video games
            const res = await req.json()
            // Set data to state and display results
            setData(res)
            setSubmitted(true)
            resetState()

        } catch(error) {
            console.error(error)
        }
    }

    return (
        <div className="Form">
            <div className="Title">
                <span>Welcome to GameREC!</span>
            </div>

            {submitted? 
                <div className="Game-List">
                    <div className="Game-List-Title">
                        Recommendations 4 You
                    </div>
                    <div onClick={() => setSubmitted(false)} className="Back-Button-1">
                        Back
                    </div>
                    
                    <CCardGroup className="Grid">
                        {data.map((item, ind) => (
                            <CCard className="Card-Style" key={ind}>
                            <CCardImage orientation="top" src="" />
                            <CCardBody>
                                <CCardTitle className="My-Card-Title">{item['Title']}</CCardTitle>
                                <CCardText style={{color: "green"}}>
                                    Genres: {item['Metadata']['Genres']}
                                </CCardText>
                                <CCardText style={{color: "purple"}}>
                                    Used Price: ${item['Metrics']['Used Price']}
                                </CCardText>
                                <CCardText style={{color: "blue"}}>
                                    Average Play Time: {
                                        Math.round(item['Length']['All PlayStyles']['Average']).toFixed(0)
                                    } Hrs
                                </CCardText>
                                <CCardText style={{color: "red"}}>
                                    {item['Features']["Online?"]? "Online" : "Offline"}
                                </CCardText>
                                <CCardText>
                                    <small className="text-medium-emphasis">
                                        By {
                                            item['Metadata']['Publishers']?
                                            item['Metadata']['Publishers']
                                            :
                                            "Unknown"}
                                    </small>
                                </CCardText>
                            </CCardBody>
                            </CCard>
                        ))}
                    </CCardGroup>
                
                    <div onClick={() => setSubmitted(false)} className="Back-Button-2">
                        Back
                    </div>
                </div>
                :
                <>
                <div>
                    <div className="Category">
                        <label className="Label">Select Your Favorite Genres</label>
                        
                        <div className="Checkbox-Container">
                            <div className="Checkbox-Column">
                                <div>
                                    <input type="checkbox"
                                        defaultChecked={false}
                                        onChange={() => toggleChecked("Action")}
                                    />
                                    Action
                                </div>
                                <label>
                                    <input type="checkbox"
                                        defaultChecked={false}
                                        onChange={() => toggleChecked("Racing / Driving")}
                                    />
                                    Racing / Driving
                                </label>
                                <div>
                                    <input type="checkbox"
                                        defaultChecked={false}
                                        onChange={() => toggleChecked("Strategy")}
                                    />
                                    Strategy
                                </div>
                                <div>
                                    <input type="checkbox"
                                        defaultChecked={false}
                                        onChange={() => toggleChecked("Sports")}
                                    />
                                    Sports
                                </div>
                            </div>
                            <div className="Checkbox-Column">
                                <div>
                                    <input type="checkbox"
                                        defaultChecked={false}
                                        onChange={() => toggleChecked("Simulation")}
                                    />
                                    Simulation
                                </div>
                                <div>
                                    <input type="checkbox"
                                        defaultChecked={false}
                                        onChange={() => toggleChecked("Adventure")}
                                    />
                                    Adventure
                                </div>
                                <div>
                                    <input type="checkbox"
                                        defaultChecked={false}
                                        onChange={() => toggleChecked("Role-Playing (RPG)")}
                                    />
                                    Role-Playing RPG
                                </div>
                                <div>
                                    <input type="checkbox"
                                        defaultChecked={false}
                                        onChange={() => toggleChecked("Educational")}
                                    />
                                    Educational
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="Category">
                        <label className="Label">Give a Price Range</label>
                        <div className="Price-Range">
                            <div>
                                <input 
                                    type="number"
                                    className="Rangebox" 
                                    placeholder="0"
                                    val={priceRange[0]}
                                    min="0"
                                    max="60"
                                    onChange={(e) => editPriceRange(0, e.target.value)}
                                />
                            </div>
                            <div>
                                <input 
                                    type="number" 
                                    className="Rangebox" 
                                    placeholder="60"
                                    val={priceRange[1]}
                                    min="0"
                                    max="60"
                                    onChange={(e) => editPriceRange(1, e.target.value)}
                                />
                            </div>
                        </div>
                    </div>       

                    <div className="Category">
                        <label className="Label">Average Time Range</label>
                        <div className="Price-Range">
                            <div>
                                <input 
                                    type="number"
                                    className="Rangebox" 
                                    placeholder="0"
                                    val={timeRange[0]}
                                    min="0"
                                    max="40"
                                    onChange={(e) => editTimeRange(0, e.target.value)}
                                />
                            </div>
                            <div>
                                <input 
                                    type="number" 
                                    className="Rangebox" 
                                    placeholder="40"
                                    val={timeRange[1]}
                                    min="0"
                                    max="40"
                                    onChange={(e) => editTimeRange(1, e.target.value)}
                                />
                            </div>
                        </div>
                    </div>

                    <div className="Category">
                        <label className="Label">Online/Offline?</label>
                        <div className="Online-Button-Wrap">
                            <div 
                                className="Online-Button"
                                style={online === 2? selectedButton : nonSelectedButton}
                                onClick={() => setOnline(2)}
                            >
                                All
                            </div>
                            <div 
                                className="Online-Button"
                                style={online === 0? selectedButton : nonSelectedButton}
                                onClick={() => setOnline(0)}
                            >
                                Offline
                            </div>
                            <div 
                                className="Online-Button"
                                style={online === 1? selectedButton : nonSelectedButton}
                                onClick={() => setOnline(1)}
                            >
                                Online
                            </div>
                        </div>
                    </div>
                            
                </div>
                <div className="Submit-Block">
                    <div className="Submit" onClick={() => submitHandler("shellsort")}>
                        {`Get Recs (Shell Sort)`}
                    </div>
                    <div className="Submit" onClick={() => submitHandler("timsort")}>
                        {`Get Recs (Tim Sort)`}
                    </div>
                </div>
                </>
            }
        </div>
    )
}

export default Form;

import React, { useState } from 'react'

let App=()=>{
  let [clr, updateColor] = useState("#FFFF00")
  let [txt, updateText] = useState("TATA")

  let update = ()=>{
    updateColor((clr)=>{
    if (clr==="#FF0000"){
        return "#FFFF00"
    } else{
        return "#FF0000"
    }
    } )
  }

  let Tu = ()=>{
    updateText((txt)=>{
    if (txt==="TATA"){
        return "BYE...BY"
    } else{
        return "TATA"
    }
    })
  }
  return(
    <>
    <button onClick={update} onMouseOver={Tu} style={{backgroundColor:clr}}>{txt}</button>
    </>
  )
}
export default App
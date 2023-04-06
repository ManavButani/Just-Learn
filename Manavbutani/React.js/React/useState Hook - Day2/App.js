import React, { useState } from 'react'

const App = ()=>{
  let newTime = new Date().toLocaleTimeString()
  let [time,setTime]=useState(newTime)

  const update=()=>{
    setTime(() => {
      let newTime = new Date().toLocaleTimeString()
      return newTime
    })
  }

  return(
    <>
    <h1>{time}</h1>
    <button onClick={update}>Update</button>
    </>
  )
}

export default App
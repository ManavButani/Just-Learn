import React, { useState } from 'react'

const App = ()=>{
  let newTime = new Date().toLocaleTimeString()
  let [time,setTime]=useState(newTime)

  let update=()=>{
    setTime(() => {
      let newTime = new Date().toLocaleTimeString()
      return newTime
    })
  }

  setInterval(update,1000)
  return(
    <>
    <h1>{time}</h1>
    </>
  )
}

export default App
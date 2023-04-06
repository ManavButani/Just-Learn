import React, { useState } from 'react'

const App = ()=>{
  let [count,setCount]=useState(0)

  const inC=()=>{
    setCount((prev) => {
      return prev+1
    })
  }

  return(
    <>
    <h1>{count}</h1>
    <button onClick={inC}>Inc</button>
    </>
  )
}

export default App
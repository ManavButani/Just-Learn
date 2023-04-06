import React, { useContext } from "react";
import { ManavContext, UserContext } from "./App";


const Cmp3 =()=>{
  let swa = useContext(ManavContext)
  let name = useContext(UserContext)

    return(
      <>
          <h1>Hello, {swa}{name}</h1>
      </>
    )
}

export default Cmp3
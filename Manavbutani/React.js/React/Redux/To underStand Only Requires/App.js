import React from "react";
import Navbar from "./Navbar";
import Counter from "./Counter";
import { useSelector } from "react-redux";

function App() {
  const state = useSelector((state) => {
    return state.changeTheNumber;
  });
  return (
    <>
      <Navbar amount={state} />
      <br />
      <Counter />
    </>
  );
}

export default App;

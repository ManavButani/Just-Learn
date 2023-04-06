import React from "react";
import Home from "./Home";
import ShowNote from "./ShowNote";
import { useSelector } from "react-redux";

const App = () => {
  const state = useSelector((state) => {
    return state.ToDoReducer;
  });
  return (
    <>
      <Home />
      <br />
      <ShowNote list={state} />
    </>
  );
};

export default App;

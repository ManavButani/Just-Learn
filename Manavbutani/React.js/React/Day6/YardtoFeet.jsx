import React, { useState } from "react";

function YardtoFeet() {
  let [SquareYard, updateSquareYard] = useState("");
  let [SquareFeet, updateSquareFeet] = useState("");

  let handleSquareYard = (event) => {
    updateSquareFeet(() => {
      return "";
    });
    updateSquareYard(() => {
      return event.target.value;
    });

    updateSquareFeet(() => {
      return event.target.value * 9;
    });
  };

  let handleSquareFeet = (event) => {
    updateSquareYard(() => {
      return "";
    });

    updateSquareFeet(() => {
      return event.target.value;
    });

    updateSquareYard(() => {
      return event.target.value / 9;
    });
  };

  return (
    <>
      <h1>SquareYard:</h1>
      <input type="text" value={SquareYard} onChange={handleSquareYard}></input>

      <h1>SquareFeet:</h1>
      <input type="text" value={SquareFeet} onChange={handleSquareFeet}></input>
    </>
  );
}

export default YardtoFeet;

import React, { useState } from "react";
import "./index.css";

let App = () => {
  let [string, setString] = useState("");

  let handleButton = (event) => {
    event.preventDefault();
    setString(string + event.target.value);
  };

  let handleCalculate = () => {
    try {
      setString(eval(string));
    } catch (e) {
      alert("Enter Valid Expression");
    }
  };

  let handleClear = () => {
    setString("");
  };
  return (
    <>
      <div className="row">
        <input className="input" type="text" value={string} onChange={(e) => {setString(e.target.value)}}/>
      </div>
      <div className="row">
        <button className="button" value={7} onClick={handleButton}>
          7
        </button>
        <button className="button" value={8} onClick={handleButton}>
          8
        </button>
        <button className="button" value={9} onClick={handleButton}>
          9
        </button>
        <button className="button" value={"*"} onClick={handleButton}>
          *
        </button>
      </div>
      <div className="row">
        <button className="button" value={4} onClick={handleButton}>
          4
        </button>
        <button className="button" value={5} onClick={handleButton}>
          5
        </button>
        <button className="button" value={6} onClick={handleButton}>
          6
        </button>
        <button className="button" value={"/"} onClick={handleButton}>
          /
        </button>
      </div>
      <div className="row">
        <button className="button" value={1} onClick={handleButton}>
          1
        </button>
        <button className="button" value={2} onClick={handleButton}>
          2
        </button>
        <button className="button" value={3} onClick={handleButton}>
          3
        </button>
        <button className="button" value={"+"} onClick={handleButton}>
          +
        </button>
      </div>
      <div className="row">
        <button className="button" value={0} onClick={handleButton}>
          0
        </button>
        <button className="button" value={"."} onClick={handleButton}>
          .
        </button>
        <button className="button" onClick={handleCalculate}>
          =
        </button>
        <button className="button" value={"-"} onClick={handleButton}>
          -
        </button>
        <button className="button" value={""} onClick={handleClear}>
          C
        </button>
      </div>
    </>
  );
};

export default App;

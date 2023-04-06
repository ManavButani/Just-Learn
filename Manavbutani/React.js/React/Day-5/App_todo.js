import React, { useState } from "react";
import ToDo from "./ToDo";

function App() {
  const [note, setNote] = useState("");
  const [final, setFinal] = useState([]);

  let handleSubmit = (event) => {
    event.preventDefault();

    setFinal((prev) => {
      if (final.includes(note)) {
        return [...prev];
      } else {
        if (note !== "") {
          return [...prev, note];
        } else {
          alert("Empty Note");
          return [...prev]
        }
      }
    });
  };

  const todoList = final.map((data,index) => <ToDo key={index} name={data} />);
  
  return (
    <>
      <input
        type="text"
        value={note}
        onChange={(event) => {
          setNote(event.target.value);
        }}
      ></input>
      <button type="submit" onClick={handleSubmit}>
        Add
      </button>
      {todoList}
    </>
  );
}

export default App;

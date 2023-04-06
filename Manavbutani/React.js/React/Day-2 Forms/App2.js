import React, { useState } from "react";

const App = () => {
  let [name, updateName] = useState("");
  let input_on_page = function (event) {
    updateName(event.target.value);
  };

  let [fullName, setFullName] = useState();
  let submit_on_page = function (event) {
    event.preventDefault() // restrict to refresh a page
    setFullName(name)
  };

  return (
    <>
      <form>
        <div>
          <input
            placeholder="Enter Your Name:"
            type="text"
            value={name}
            onChange={input_on_page}
          ></input>
          <button type="submit" onClick={submit_on_page}>
            Submit
          </button>
        </div>
      </form>
      <h2>Welcome {fullName} </h2>
    </>
  );
};

export default App;
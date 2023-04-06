import React, { useState } from "react";

const App = () => {
  let [name, updateName] = useState("");
  let input_on_page = function (event) {
    updateName(event.target.value);
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
          <button type="submit">Submit</button>
        </div>
      </form>
      <h2>Welcome {name} </h2>
    </>
  );
};

export default App;

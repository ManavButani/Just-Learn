import React, { useState } from "react";

const App = () => {
  let data = [
    {
      name: "Manav",
      password: "123",
    },
    {
      name: "Krenil",
      password: "1213",
    },
    {
      name: "Shyam",
      password: "1234",
    },
    {
      name: "Krupal",
      password: "456",
    },
  ];

  let [name, updateName] = useState("");
  let input_on_page = function (event) {
    updateName(event.target.value);
  };

  let [fullName, setFullName] = useState(null);
  let submit_on_page = function (event) {
    event.preventDefault(); // restrict to refresh a page
    const user = data.find((user) => user.name === name);

    // data is our list/array
    // find is inbuilt method
    // which takes function as a argument
    // return value based on function condition
    // if function doesn't satisfied condition then returns null

    if (user) {
      setFullName(name);
    } else {
      setFullName(null);
    }
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
      {fullName != null ? <h2>Welcome {fullName}</h2> : null}
    </>
  );
};
export default App;

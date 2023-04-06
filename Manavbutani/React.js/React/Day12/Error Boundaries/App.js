import React, { useRef, useState } from "react";
import CheckData from "./CheckData";
import ErrorBoundaries from "./ErrorBoundaries";

const App = () => {
  const email = useRef("");
  const password = useRef("");

  const [loading, setLoading] = useState([]);
  let handleData = () => {
    setLoading([email.current.value, password.current.value]);
  };

  return (
    <>
      Email:
      <input
        type="text"
        ref={email}
        onChange={(event) => {
          return event.target.value;
        }}
      />
      <br />
      Password:
      <input
        type="text"
        ref={password}
        onChange={(event) => {
          return event.target.value;
        }}
      />
      <br />
      <button type="submit" onClick={handleData}>
        Login
      </button>
      <ErrorBoundaries>
        <CheckData frontside_data={loading} />
      </ErrorBoundaries>
    </>
  );
};

export default App;

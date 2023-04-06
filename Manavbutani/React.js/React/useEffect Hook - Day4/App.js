import React, { useEffect, useState } from "react";

let App = () => {
  let [first, setFirst] = useState(0);

  let count;
  if (first === 5 || first === 10 || first === 15) {
    count++;
  }
  let OK = () => {
    first++;
    setFirst(first);
  };

  useEffect(() => {
    alert("Ohho...");
  }, [count]);
  return (
    <>
      <button onClick={OK}>Increament {first}</button>
    </>
  );
};

export default App;

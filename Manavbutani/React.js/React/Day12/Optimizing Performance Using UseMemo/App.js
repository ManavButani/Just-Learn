import React, { useMemo, useState } from "react";

const App = () => {
  const [counterOne, setCounterOne] = useState(0);
  const [counterTwo, setCounterTwo] = useState(0);

  let handleOne = () => {
    setCounterOne((prev) => {
      return prev + 1;
    });
  };

  let handleTwo = () => {
    setCounterTwo((prev) => {
      return prev + 1;
    });
  };

  const evenOdd = useMemo(() => {
    let i = 0;
    while (i < 999999999) i++;
    if (counterOne % 2 === 0) {
      return true;
    } else {
      return false;
    }
  }, [counterOne]);

  return (
    <div>
      <button type="submit" onClick={handleOne}>
        CounterOne - {counterOne}
      </button>
      {evenOdd ? "Even" : "Odd"}
      <br />
      <button type="submit" onClick={handleTwo}>
        CounterTwo - {counterTwo}
      </button>
    </div>
  );
};

export default App;

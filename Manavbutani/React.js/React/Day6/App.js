import React, { useState } from "react";
import KmMiles from "./KmMiles";
import KGtoLiters from "./KGtoLiters";
import YardtoFeet from "./YardtoFeet";

function App() {
  let [kmtomiles, setKmtomiles] = useState(false);
  let handleKMtoMiles = () => {
    setKmtomiles(true);
    setKgtoliters(false);
    setFeettoyard(false);
  };

  let [kgtoliters, setKgtoliters] = useState(false);
  let handleKgtoliters = () => {
    setKgtoliters(true);
    setKmtomiles(false);
    setFeettoyard(false);
  };

  let [feettoyard, setFeettoyard] = useState(false);
  let handleFeettoyard = () => {
    setFeettoyard(true);
    setKgtoliters(false);
    setKmtomiles(false);
  };
  return (
    <div>
      <button type="submit" onClick={handleKMtoMiles}>
        Km to Miles
      </button>
      <button type="submit" onClick={handleKgtoliters}>
        KG to Liter
      </button>
      <button type="submit" onClick={handleFeettoyard}>
        Feet to Yard
      </button>
      {kmtomiles ? <KmMiles /> : <br />}
      {kgtoliters ? <KGtoLiters /> : <br />}
      {feettoyard ? <YardtoFeet /> : <br />}
    </div>
  );
}

export default App;

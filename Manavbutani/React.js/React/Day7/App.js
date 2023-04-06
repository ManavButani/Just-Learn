import data from "./information.json";
import React from "react";
import Styler from "./Styler";

const App = () => {
  return (
    <>
      {/* <div>
        {JSON.stringify(data)}
        <br />
        <br />
        {JSON.stringify(data["data"])}
        <br />
        <br />
        {JSON.stringify(data["data"][0]["id"])}
      </div> */}
      {data.data.map((product) => {
        return <Styler product={product} />;
      })}
    </>
  );
};

export default App;

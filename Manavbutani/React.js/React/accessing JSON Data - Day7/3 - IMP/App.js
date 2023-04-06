import data from "./country.json";
import React from "react";

const App = () => {
  return (
    <>
      <div>
        <div>Name : {data.name}</div>
        <div>Email : {data.email}</div>
        <div>Website : {data.website}</div>
        {/* <div>{data.country}</div> This line breaks the code */}
        <div>
          <label>Country :</label>
          <select>
            {data.country.map((country) => {
              return (
                <option key={country.id} value={country.id}>
                  {country.name}
                </option>
              );
            })}
          </select>
        </div>
      </div>
    </>
  );
};

export default App;

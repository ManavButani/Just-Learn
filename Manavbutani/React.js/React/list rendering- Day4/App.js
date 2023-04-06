import React from "react";
import Person from "./Person";

function App() {
  let person = [
    { name: "Manav", Age: 22 },
    { name: "Ghanshyam", Age: 6 },
    { name: "Swaminaryaa=n", Age: 25 },
    { name: "Krenil", Age: 18 },
  ];

  const personList = person.map(p=> <Person obj={p}/>)
  return (<>
  {personList}
  </>);
}

export default App;

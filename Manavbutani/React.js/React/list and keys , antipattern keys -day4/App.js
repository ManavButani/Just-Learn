// if children wants to access key then it will shows undefined 
import React from "react";
import Person from "./Person";

function App() {
  let person = [
    { name: "Manav", Age: 22 },
    { name: "Ghanshyam", Age: 6 },
    { name: "Swaminaryaa=n", Age: 25 },
    { name: "Krenil", Age: 18 },
  ];

  const personList = person.map((p,index)=> <Person key={index} obj={p}/>)
  return (<>
  {personList}
  </>);
}


export default App;

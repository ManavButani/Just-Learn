import React from "react";
import ToDo from "./ToDo";

const ShowNote = (props) => {
  let newVar = props;
  const todoList = newVar.list.map((data, index) => (
    <ToDo key={index} name={data} location={index}></ToDo>
  ));
  return <>{todoList}</>;
};

export default ShowNote;

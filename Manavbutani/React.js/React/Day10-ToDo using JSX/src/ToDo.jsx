import { useDispatch } from "react-redux";
import React from "react";
import { deleteNote } from "./state/action";

function ToDo({ name, location }) {
  const dispatch = useDispatch();
  let handleDelete = () => {
    console.log(location);
    dispatch(deleteNote(location));
  };
  return (
    <div key={location}>
      <br />
      <ul>
        <li>{name}</li>
        <button type="submit" onClick={handleDelete}>
          Delete
        </button>
      </ul>
    </div>
  );
}

export default ToDo;

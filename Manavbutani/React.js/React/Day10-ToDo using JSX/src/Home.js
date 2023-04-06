import React, { useRef } from "react";
import { useDispatch } from "react-redux";
import { addNote } from "./state/action";

const Home = () => {
  let note = useRef("");
  const dispatch = useDispatch();

  let handleNote = () => {
    dispatch(addNote(note.current.value));
  };
  return (
    <div>
      <input
        type="text"
        onChange={(event) => {
          return event.target.value;
        }}
        ref={note}
      />
      <button type="submit" onClick={handleNote}>
        Add
      </button>
    </div>
  );
};

export default Home;

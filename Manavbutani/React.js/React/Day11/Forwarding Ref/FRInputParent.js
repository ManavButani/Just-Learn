import React from "react";
import FRInput from "./FRInput";

const FRInputParent = () => {
  let inputRef = React.createRef();

  let clickHandler = () => {
    inputRef.current.focus();
  };

  return (
    <>
      <FRInput ref={inputRef} />
      <button onClick={clickHandler}> Focus </button>
    </>
  );
};

export default FRInputParent;

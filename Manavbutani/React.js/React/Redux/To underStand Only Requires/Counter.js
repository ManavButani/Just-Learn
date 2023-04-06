import React from "react";
import { useDispatch } from "react-redux";
import { incAmount, decAmount } from "./state/action-creators";

const Counter = () => {
  const dispatch = useDispatch();
  return (
    <div>
      <button
        type="button"
        class="btn btn-primary"
        onClick={() => dispatch(incAmount())}
      >
        +
      </button>
      Up/Down
      <button
        type="button"
        class="btn btn-secondary"
        onClick={() => dispatch(decAmount())}
      >
        --
      </button>
    </div>
  );
};

export default Counter;

export const incAmount = () => {
  return { type: "Increment", payload: 100 };
};

export const decAmount = () => {
  return { type: "Decrement", payload: 100 };
};

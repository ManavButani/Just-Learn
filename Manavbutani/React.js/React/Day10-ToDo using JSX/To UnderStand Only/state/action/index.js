export const addNote = (args) => {
  return {
    type: "Add",
    payload: args,
  };
};

export const deleteNote = (args) => {
  return {
    type: "Delete",
    payload: args,
  };
};

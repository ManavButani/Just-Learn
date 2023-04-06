let initialState = [];

const ToDoReducer = (state = initialState, action) => {
  switch (action.type) {
    case "Add":
      return [...state, action.payload];

    case "Delete":
      console.log(state);
      const newList = state
        .slice(0, action.payload)
        .concat(state.slice(action.payload + 1));
      return [...newList];

    default:
      return [...state];
  }
};

export default ToDoReducer;

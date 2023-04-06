import { combineReducers } from "redux";
import ToDoReducer from "./addDelete";

const rootReducer = combineReducers({
  ToDoReducer,
});

export default rootReducer;

import rootReducer from "./state/reducer";
import { configureStore } from "@reduxjs/toolkit";

let store = configureStore({
  reducer: rootReducer,
});
export default store;

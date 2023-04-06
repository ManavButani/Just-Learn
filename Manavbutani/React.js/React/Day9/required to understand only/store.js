import { configureStore } from "@reduxjs/toolkit";
import rootReducer from "./state/reducer";

const store = configureStore({ reducer: rootReducer });

export default store;

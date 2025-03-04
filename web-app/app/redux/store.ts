import { configureStore } from "@reduxjs/toolkit";
import predictionsReducer from "./predictionsSlice";
import matchesReducer from "./bestSlice";

export const store = configureStore({
  reducer: {
    predictions: predictionsReducer,
    matches: matchesReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

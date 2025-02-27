import { configureStore } from "@reduxjs/toolkit";
import predictionsReducer from "./predictionsSlice";

export const store = configureStore({
  reducer: {
    predictions: predictionsReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

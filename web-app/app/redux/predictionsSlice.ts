import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

interface Match {
  id: number;
  homeTeam: string;
  awayTeam: string;
  prediction: string;
  odds: string;
  result: string;
  reason: string;
  chance: string;
  time: string;
}

interface League {
  league: string;
  matches: Match[];
}

interface PredictionsState {
  data: League[];
  selectedMatch: Match | null;
  lastFetched: number | null;
}

const initialState: PredictionsState = {
  data: [],
  selectedMatch: null,
  lastFetched: null,
};

// Async thunk to fetch data
export const fetchPredictions = createAsyncThunk(
  "predictions/fetchPredictions",
  async (_, { dispatch }) => {
    const storedData = localStorage.getItem("predictionsData");
    const storedTimestamp = localStorage.getItem("predictionsTimestamp");
    const lastFetched = storedTimestamp ? parseInt(storedTimestamp, 10) : 0;

    const oneDay = 24 * 60 * 60 * 1000; // 1 day in ms
    const now = Date.now();

    // If data exists and is fresh, use localStorage
    if (storedData && now - lastFetched < oneDay) {
        console.log("Using cached data");
        dispatch(setPredictions(JSON.parse(storedData)));
        return;
    }

    // Check if we need to update
    const response = await fetch("http://127.0.0.1:5000/status");
    const shouldUpdate  = await response.json();

    if (shouldUpdate.status || !storedData) {
      console.log("Fetching new data from backend");
      const dataResponse = await fetch("http://127.0.0.1:5000/ovr-predictions");
      const data = await dataResponse.json();
      // Store in localStorage
      localStorage.setItem("predictionsData", JSON.stringify(data));
      localStorage.setItem("predictionsTimestamp", now.toString());

      dispatch(setPredictions(data));
    }
  }
);

const predictionsSlice = createSlice({
  name: "predictions",
  initialState,
  reducers: {
    setPredictions: (state, action: PayloadAction<League[]>) => {
      state.data = action.payload;
      state.lastFetched = Date.now();
    },
    setSelectedMatch: (state, action: PayloadAction<Match | null>) => {
      state.selectedMatch = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(fetchPredictions.fulfilled, (state) => {
      console.log("Predictions fetched successfully");
    });
  },
});

export const { setPredictions, setSelectedMatch } = predictionsSlice.actions;
export default predictionsSlice.reducer;

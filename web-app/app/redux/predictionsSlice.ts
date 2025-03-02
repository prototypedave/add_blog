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
  async (_, { dispatch, getState }) => {
    const storedData = localStorage.getItem("predictionsData");
    const storedTimestamp = localStorage.getItem("predictionsTimestamp");
    const lastFetched = storedTimestamp ? parseInt(storedTimestamp, 10) : 0;

    const oneDay = 24 * 60 * 60 * 1000; // 1 day in ms
    const now = Date.now();
    const fiveUTC = new Date();
    fiveUTC.setUTCHours(5, 0, 0, 0);

    const state: any = getState(); // Get current state from Redux store
    const currentData = state.predictions.data; // Current store data

    // If data is already fetched today and it's past 5 UTC, prevent further calls
    if (storedData && now - lastFetched < oneDay && now < fiveUTC.getTime()) {
      console.log("Using cached data, preventing API call");
      dispatch(setPredictions(JSON.parse(storedData)));
      return;
    }

    let attempts = 0;
    let shouldFetch = false;
    let apiData: League[] | null = null;

    while (attempts < 3) {
      const response = await fetch("https:prototypedave.site/api/status");
      const statusData = await response.json();

      if (statusData.status) {
        console.log(`Fetching new data, attempt ${attempts + 1}`);
        const dataResponse = await fetch("https:prototypedave.site/api/ovr-predictions");
        apiData = await dataResponse.json();

        if (JSON.stringify(apiData) !== JSON.stringify(currentData)) {
          shouldFetch = true;
          break; // Stop polling if data changes
        }
      }

      if (attempts < 2) {
        await new Promise((resolve) => setTimeout(resolve, 10 * 60 * 1000)); // Wait 10 minutes
      }
      
      attempts++;
    }

    if (shouldFetch && apiData) {
      console.log("Updating store with new data");
      localStorage.setItem("predictionsData", JSON.stringify(apiData));
      localStorage.setItem("predictionsTimestamp", now.toString());
      dispatch(setPredictions(apiData));
    } else {
      console.log("No data changes detected, preventing API call until 5 UTC next day");
      localStorage.setItem("predictionsTimestamp", fiveUTC.getTime().toString());
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

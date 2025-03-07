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
  won: boolean;
}

interface League {
  league: string;
  matches: Match[];
}

interface PredictionsState {
  data: League[];
  previousData: League[];
  selectedMatch: Match | null;
  lastFetched: number | null;
}

const initialState: PredictionsState = {
  data: [],
  previousData: [],
  selectedMatch: null,
  lastFetched: null,
};

// Fetch predictions (optimized)
export const fetchPredictions = createAsyncThunk(
  "predictions/fetchPredictions",
  async (_, { dispatch, getState }) => {
    const storedData = localStorage.getItem("predictionsData");
    const storedTimestamp = localStorage.getItem("predictionsTimestamp");
    const lastFetched = storedTimestamp ? parseInt(storedTimestamp, 10) : 0;

    const now = Date.now();
    const fiveUTC = new Date();
    fiveUTC.setUTCHours(5, 0, 0, 0);
    const oneDay = 24 * 60 * 60 * 1000; // 1 day in milliseconds

    const state: any = getState();
    const currentData = state.predictions.data;

    // Use cached data if it's still valid
    if (storedData && now - lastFetched < oneDay && now < fiveUTC.getTime()) {
      console.log("Using cached data for today's predictions");
      dispatch(setPredictions(JSON.parse(storedData)));
      return;
    }

    try {
      const response = await fetch("http://localhost:5001/api/football/general");
      const apiData: League[] = await response.json();

      // Only update if new data is different
      if (JSON.stringify(apiData) !== JSON.stringify(currentData)) {
        console.log("New predictions found, updating...");
        localStorage.setItem("predictionsData", JSON.stringify(apiData));
        localStorage.setItem("predictionsTimestamp", now.toString());
        dispatch(setPredictions(apiData));
      } else {
        console.log("No data changes detected, preventing redundant updates");
        localStorage.setItem("predictionsTimestamp", fiveUTC.getTime().toString());
      }
    } catch (error) {
      console.error("Failed to fetch today's predictions:", error);
    }
  }
);

// Fetch previous predictions (optimized)
export const fetchPreviousPredictions = createAsyncThunk(
  "predictions/fetchPreviousPredictions",
  async (_, { dispatch }) => {
    const storedPreviousData = localStorage.getItem("previousPredictions");

    if (storedPreviousData) {
      console.log("Using cached previous predictions");
      dispatch(setPreviousPredictions(JSON.parse(storedPreviousData)));
      return;
    }

    try {
      const response = await fetch("http://localhost:5001/api/football/general/previous");
      const data: League[] = await response.json();

      console.log("Fetched previous predictions");
      localStorage.setItem("previousPredictions", JSON.stringify(data));
      dispatch(setPreviousPredictions(data));
    } catch (error) {
      console.error("Failed to fetch previous predictions:", error);
    }
  }
);

const predictionsSlice = createSlice({
  name: "predictions",
  initialState,
  reducers: {
    setPredictions: (state, action: PayloadAction<League[]>) => {
      if (state.data.length > 0) {
        state.previousData = JSON.parse(JSON.stringify(state.data)); // Create a deep copy
        localStorage.setItem("previousPredictions", JSON.stringify(state.previousData));
      }
      state.data = action.payload;
      state.lastFetched = Date.now();
    },
        
    setPreviousPredictions: (state, action: PayloadAction<League[]>) => {
      state.previousData = action.payload;
    },
    setSelectedMatch: (state, action: PayloadAction<Match | null>) => {
      state.selectedMatch = action.payload;
    },
    clearPreviousPredictions: (state) => {
      state.previousData = [];
      localStorage.removeItem("previousPredictions");
    },
  },
  extraReducers: (builder) => {
    builder.addCase(fetchPredictions.fulfilled, () => {
      console.log("Today's predictions fetched successfully");
    });
    builder.addCase(fetchPreviousPredictions.fulfilled, () => {
      console.log("Previous predictions fetched successfully");
    });
  },
});

export const {
  setPredictions,
  setPreviousPredictions,
  setSelectedMatch,
  clearPreviousPredictions,
} = predictionsSlice.actions;

export default predictionsSlice.reducer;

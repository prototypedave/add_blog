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
  data: League[]; // Stores today's predictions
  previousData: League[]; // Stores previous predictions
  selectedMatch: Match | null;
  lastFetched: number | null;
}

const initialState: PredictionsState = {
  data: [],
  previousData: [],
  selectedMatch: null,
  lastFetched: null,
};

// Fetch today's predictions
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

    const state: any = getState();
    const currentData = state.predictions.data;

    if (storedData && now - lastFetched < oneDay && now < fiveUTC.getTime()) {
      console.log("Using cached data for today's predictions");
      dispatch(setPredictions(JSON.parse(storedData)));
      return;
    }

    let attempts = 0;
    let shouldFetch = false;
    let apiData: League[] | null = null;

    while (attempts < 3) {
      const response = await fetch("https://prototypedave.site/api/status");
      const statusData = await response.json();

      if (statusData.status) {
        console.log(`Fetching new data, attempt ${attempts + 1}`);
        const dataResponse = await fetch("https://prototypedave.site/api/ovr-predictions");
        apiData = await dataResponse.json();

        if (JSON.stringify(apiData) !== JSON.stringify(currentData)) {
          shouldFetch = true;
          break;
        }
      }

      if (attempts < 2) {
        await new Promise((resolve) => setTimeout(resolve, 10 * 60 * 1000));
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

// Fetch previous predictions
export const fetchPreviousPredictions = createAsyncThunk(
  "predictions/fetchPreviousPredictions",
  async (_, { dispatch }) => {
    const storedPreviousData = localStorage.getItem("previousPredictions");

    if (storedPreviousData) {
      console.log("Using cached data for previous predictions");
      dispatch(setPreviousPredictions(JSON.parse(storedPreviousData)));
      return;
    }

    try {
      const response = await fetch("https://prototypedave.site/api/previous-predictions");
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
      state.data = action.payload;
      state.lastFetched = Date.now();
    },
    setPreviousPredictions: (state, action: PayloadAction<League[]>) => {
      state.previousData = action.payload;
    },
    setSelectedMatch: (state, action: PayloadAction<Match | null>) => {
      state.selectedMatch = action.payload;
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

export const { setPredictions, setPreviousPredictions, setSelectedMatch } = predictionsSlice.actions;
export default predictionsSlice.reducer;

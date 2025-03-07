import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

interface Match {
  id: number;
  homeTeam: string;
  awayTeam: string;
  prediction: string;
  odds: string;
  result: string;
  time: string;
  won: boolean;
}

interface League {
  league: string;
  matches: Match[];
}

interface BasketState {
  data: League[];
  previousData: League[];
  selectedMatch: Match | null;
  lastFetched: number | null;
}

const initialState: BasketState = {
  data: [],
  previousData: [],
  selectedMatch: null,
  lastFetched: null,
};


export const fetchBasketPredictions = createAsyncThunk(
  "predictions/fetchBasketPredictions",
  async (_, { dispatch, getState }) => {
    const storedData = localStorage.getItem("basketData");
    const storedTimestamp = localStorage.getItem("basketTimestamp");
    const lastFetched = storedTimestamp ? parseInt(storedTimestamp, 10) : 0;

    const now = Date.now();
    const fiveUTC = new Date();
    fiveUTC.setUTCHours(5, 0, 0, 0);
    const oneDay = 24 * 60 * 60 * 1000; 

    const state: any = getState();
    const currentData = state.predictions.data;

    // Use cached data if it's still valid
    if (storedData && now - lastFetched < oneDay && now < fiveUTC.getTime()) {
      console.log("Using cached data for today's predictions");
      dispatch(setBasket(JSON.parse(storedData)));
      return;
    }

    try {
      const response = await fetch("http://localhost:5001/api/basketball/general");
      const apiData: League[] = await response.json();

      // Only update if new data is different
      if (JSON.stringify(apiData) !== JSON.stringify(currentData)) {
        console.log("New predictions found, updating...");
        localStorage.setItem("basketData", JSON.stringify(apiData));
        localStorage.setItem("basketTimestamp", now.toString());
        dispatch(setBasket(apiData));
      } else {
        console.log("No data changes detected, preventing redundant updates");
        localStorage.setItem("basketTimestamp", fiveUTC.getTime().toString());
      }
    } catch (error) {
      console.error("Failed to fetch today's predictions:", error);
    }
  }
);

// Fetch previous predictions (optimized)
export const fetchPreviousBasketballPredictions = createAsyncThunk(
  "predictions/fetchPreviousPredictions",
  async (_, { dispatch }) => {
    const storedPreviousData = localStorage.getItem("previousBasket");

    if (storedPreviousData) {
      console.log("Using cached previous predictions");
      dispatch(setPreviousBasket(JSON.parse(storedPreviousData)));
      return;
    }

    try {
      const response = await fetch("http://localhost:5001/api/basketball/general/previous");
      const data: League[] = await response.json();

      console.log("Fetched previous predictions");
      localStorage.setItem("previousBasket", JSON.stringify(data));
      dispatch(setPreviousBasket(data));
    } catch (error) {
      console.error("Failed to fetch previous predictions:", error);
    }
  }
);

const basketSlice = createSlice({
  name: "basket",
  initialState,
  reducers: {
    setBasket: (state, action: PayloadAction<League[]>) => {
      if (state.data.length > 0) {
        state.previousData = JSON.parse(JSON.stringify(state.data)); // Create a deep copy
        localStorage.setItem("previousBasket", JSON.stringify(state.previousData));
      }
      state.data = action.payload;
      state.lastFetched = Date.now();
    },
        
    setPreviousBasket: (state, action: PayloadAction<League[]>) => {
      state.previousData = action.payload;
    },
    setSelectedMatch: (state, action: PayloadAction<Match | null>) => {
      state.selectedMatch = action.payload;
    },
    clearPreviousBasket: (state) => {
      state.previousData = [];
      localStorage.removeItem("previousBasket");
    },
  },
  extraReducers: (builder) => {
    builder.addCase(fetchBasketPredictions.fulfilled, () => {
      console.log("Today's predictions fetched successfully");
    });
    builder.addCase(fetchPreviousBasketballPredictions.fulfilled, () => {
      console.log("Previous predictions fetched successfully");
    });
  },
});

export const {
  setBasket,
  setPreviousBasket,
  setSelectedMatch,
  clearPreviousBasket,
} = basketSlice.actions;

export default basketSlice.reducer;

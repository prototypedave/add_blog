import { createSlice } from "@reduxjs/toolkit";
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
}

interface League {
  league: string;
  matches: Match[];
}

interface PredictionsState {
  data: League[];
  selectedMatch: Match | null;
}

const initialState: PredictionsState = {
  data: [],
  selectedMatch: null,
};

const predictionsSlice = createSlice({
  name: "predictions",
  initialState,
  reducers: {
    setPredictions: (state, action: PayloadAction<League[]>) => {
      state.data = action.payload;
    },
    setSelectedMatch: (state, action: PayloadAction<Match | null>) => {
      state.selectedMatch = action.payload;
    },
  },
});

export const { setPredictions, setSelectedMatch } = predictionsSlice.actions;
export default predictionsSlice.reducer;

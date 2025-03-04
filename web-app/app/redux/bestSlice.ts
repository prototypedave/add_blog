import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

export interface Match {
  id: number;
  homeTeam: string;
  awayTeam: string;
  prediction: string; // Renamed from 'prediction'
  odds: string;
  result: string;
  reason: string;
  chance: string;
  time: string;
}

export interface League {
  league: string;
  matches: Match[];
}

interface MatchesState {
  data: League[];
  loading: boolean;
  error: string | null;
}

// Load from localStorage
const loadFromLocalStorage = (): League[] => {
  try {
    const storedData = localStorage.getItem("matches");
    return storedData ? JSON.parse(storedData) : [];
  } catch (error) {
    console.error("Error loading matches from localStorage:", error);
    return [];
  }
};

// Async thunk to fetch match data
export const fetchMatches = createAsyncThunk("matches/fetch", async () => {
  const response = await fetch("https://prototypedave.site/api/best-predictions");
  const data: League[] = await response.json();

  // Save to localStorage
  localStorage.setItem("matches", JSON.stringify(data));

  return data;
});

const initialState: MatchesState = {
  data: loadFromLocalStorage(),
  loading: false,
  error: null,
};

const matchesSlice = createSlice({
  name: "matches",
  initialState,
  reducers: {
    clearMatches: (state) => {
      state.data = [];
      localStorage.removeItem("matches");
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchMatches.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchMatches.fulfilled, (state, action) => {
        state.loading = false;
        state.data = action.payload;
      })
      .addCase(fetchMatches.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || "Failed to fetch data";
      });
  },
});

export const { clearMatches } = matchesSlice.actions;
export default matchesSlice.reducer;

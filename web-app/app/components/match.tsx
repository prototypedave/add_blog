import { useSelector, useDispatch } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { type RootState } from "../redux/store";
import { setSelectedMatch } from "../redux/predictionsSlice";
import Navbar from "~/components/navbar";
import VIPBanner from "./banner";

const MatchDetails: React.FC = () => {
  const { matchId } = useParams(); // Get match ID from URL
  const dispatch = useDispatch();
  const navigate = useNavigate();

  // Get match from Redux
  const selectedMatch = useSelector((state: RootState) => state.predictions.selectedMatch);
  const [loading, setLoading] = useState(false);

  // Fetch match if missing
  useEffect(() => {
    if (!selectedMatch && matchId) {
      setLoading(true);
      fetch(`/api/matches/${matchId}`)  // Replace with actual API endpoint
        .then((res) => res.json())
        .then((data) => {
          dispatch(setSelectedMatch(data));
        })
        .catch((err) => console.error("Error fetching match:", err))
        .finally(() => setLoading(false));
    }
  }, [matchId, selectedMatch, dispatch]);

  // Adsense script
  useEffect(() => {
    const script = document.createElement("script");
    script.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1933580054760576";
    script.async = true;
    script.crossOrigin = "anonymous";
    document.head.appendChild(script);

    return () => {
      document.head.removeChild(script);
    };
  }, []);

  if (loading) return <div className="h-screen flex items-center justify-center">Loading...</div>;

  if (!selectedMatch) {
    return (
      <div className="flex flex-col items-center justify-center h-screen">
        <p className="text-lg font-semibold">No match selected</p>
        <button
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
          onClick={() => navigate(-1)}
        >
          Go Back
        </button>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-2 pt-[55px]">
      <Navbar />
      <div className="mt-6 sm:m-0">
        <VIPBanner />
      </div>
      <div className="flex flex-row gap-4">
        <div className="p-4 sm:w-3/4">
          <div className="text-xs sm:text-base border rounded-lg p-4 shadow-md">
            <h1 className="text-base sm:text-xl font-bold pl-4 mb-4">
              {selectedMatch.homeTeam} vs {selectedMatch.awayTeam}
            </h1>
            <h3><strong>Analysis:</strong></h3>
            <p className="pl-4 mb-4">{selectedMatch.reason}</p>
            <div className="flex flex-row gap-4 justify-around">
              <p className="border rounded-md p-2"><strong>Pick:</strong> {selectedMatch.prediction}</p>
              <p className="border rounded-md p-2"><strong>Odds:</strong> {selectedMatch.odds}</p>
            </div>
          </div>
          <div className="flex justify-end mt-4">
            <button
              className="px-4 py-2 bg-blue-500 text-white rounded text-center"
              onClick={() => {
                dispatch(setSelectedMatch(null)); 
                navigate(-1);
              }}
            >
              Go Back
            </button>
          </div>
        </div>
        <div className="sm:w-full"></div>
      </div>
    </div>
  );
};

export default MatchDetails;

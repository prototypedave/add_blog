import { useSelector, useDispatch } from "react-redux";
import type { RootState } from "../redux/store";
import Navbar from "~/components/navbar";
import { useNavigate } from "react-router-dom";
import { setSelectedMatch } from "../redux/predictionsSlice";

const MatchDetails: React.FC = () => {
  const selectedMatch = useSelector((state: RootState) => state.predictions.selectedMatch);
  const navigate = useNavigate();
  const dispatch = useDispatch();

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
      <div className="flex flex-col mt-4 bg-yellow-300 items-center text-center py-4">
        <p>Google Ad Placeholder</p>
        <p>Join our VIP subscription for well analyzed accumulator matches with good winning rate!</p>
      </div>
      <div className="flex flex-row gap-4">
        <div className="p-4 w-3/4">
            <h1 className="text-xl font-bold pl-4 mb-4">{selectedMatch.homeTeam} vs {selectedMatch.awayTeam}</h1>
            <div className="border rounded-lg p-4 shadow-md">
            <h3><strong>Analysis:</strong></h3>
            <p className="pl-4 mb-4">{selectedMatch.reason}</p>
            <div className="flex flex-row gap-4 justify-around">
                <p className="border rounded-md p-2"><strong>Pick:</strong> {selectedMatch.prediction}</p>
                <p className="border rounded-md p-2"><strong>Odds:</strong> {selectedMatch.odds}</p>
            </div>
            </div>

            <button
            className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
            onClick={() => {
                dispatch(setSelectedMatch(null));
                navigate(-1);
            }}
            >
            Go Back
            </button>
        </div>
        <div className="flex flex-col mt-4 bg-yellow-300 items-center text-center py-4">
          <p>Google Ad Placeholder</p>
          <p>Join our VIP subscription for well analyzed accumulator matches with good winning rate!</p>
        </div>
      </div>
      <div className="flex flex-col mt-4 bg-yellow-300 items-center text-center py-4">
        <p>Google Ad Placeholder</p>
        <p>Join our VIP subscription for well analyzed accumulator matches with good winning rate!</p>
      </div>
    </div>
  );
};

export default MatchDetails;

import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchPredictions, setSelectedMatch, fetchPreviousPredictions } from "../redux/predictionsSlice";
import type { RootState, AppDispatch } from "../redux/store";
import Navbar from "~/components/navbar";
import VIPBanner from "~/components/banner";
import SureTipsAd from "~/components/notify";
import BetForm from "~/components/trackRecord";
import BestPick from "~/components/bestPicks";

const Football: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const predictions = useSelector((state: RootState) => state.predictions.data);
  const prevPredictions = useSelector((state: RootState) => state.predictions.previousData);
  const [isPrevious, setIsPrevious] = useState(false);
  const [nextPred, setNextPred] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (isPrevious && prevPredictions.length === 0) {
      dispatch(fetchPreviousPredictions());
    } else if (!isPrevious && predictions.length === 0) {
      dispatch(fetchPredictions());
    }
  }, [dispatch, isPrevious, prevPredictions, predictions]);

  const handlePrev = () => {
    if (nextPred) {
      setNextPred(false);
    } else {
      setIsPrevious(true);
    }
  };

  const handleNext = () => {
    if (isPrevious) {
      setIsPrevious(false);
    } else {
      setNextPred(true);
    }
  };

  const today = new Date();
  const displayedDate = new Date();
  if (isPrevious) {
    displayedDate.setDate(today.getDate() - 1); 
  }
  else if (nextPred) {
    displayedDate.setDate(today.getDate() + 1);
  }
  const formattedDate = displayedDate.toISOString().split('T')[0];

  return (
    <div className="flex flex-col gap-2 pt-[25px] bg-gray-900 lg:px-[80px]">
      <Navbar />
      <div className="flex flex-col lg:grid lg:grid-cols-5 gap-4 w-full">
        <div className="flex flex-col gap-4 px-4 lg:px-0">
          <SureTipsAd />
          <BetForm />
        </div>

        <div className="col-span-3">
          <div className="w-full bg-gray-800 shadow-lg relative p-4">
            <div className="flex justify-between text-sm py-2">
              <button
                className="cursor-pointer h-8 px-2 bg-yellow-500 text-gray-900 font-semibold rounded-sm"
                onClick={handlePrev}
              >
                <span className="px-1 text-xs">&lt;&lt;</span>Prev
              </button>
              <div className="text-center text-yellow-400">
                <h3>Football Betting Tips - {formattedDate}</h3>
                <h2 className="font-bold text-lg">{formattedDate}</h2>
              </div>
              <button
                className="cursor-pointer h-8 px-2 bg-yellow-500 text-gray-900 font-semibold rounded-sm"
                onClick={handleNext}
              >
                Next<span className="px-1 text-xs">&gt;&gt;</span>
              </button>
            </div>
            <div className="lg:border lg:border-gray-900"></div>
              {nextPred && (
                <p>Stay tuned!</p>
              )}
              {!nextPred && !isPrevious &&
                predictions.map((league) => (
                  <div key={league.league} className="mb-6">
                    <h2 className="text-sm capitalize text-white p-2">
                      <span className="font-bold  sm:text-base">
                        {league.league.split(":")[0]}:
                      </span>{" "}
                      {league.league.split(":")[1]}
                    </h2>

                    {/* Responsive Table */}
                    <div className="overflow-x-auto">
                      <table className="w-full mt-2 mb-2 text-xs sm:text-base border-separate border-spacing-0 min-w-[400px]">
                        <thead className="bg-gray-900 text-xs text-green-400">
                          <tr>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Time</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Match</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Prediction</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Odds</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">%</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Results</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Won</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-700">
                          {league.matches.map((match) => (
                            <tr
                              key={match.id}
                              className="cursor-pointer text-xs even:bg-gray-800 odd:bg-gray-700 text-white hover:bg-green-800 hover:text-black"
                              onClick={() => {
                                dispatch(setSelectedMatch(match));
                                navigate(`/predictions/${match.id}`);
                              }}
                            >
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.time}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.homeTeam} v {match.awayTeam}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.prediction}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.odds}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.chance}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.result}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">
                                {match.won ? "Win" : match.result !== "-" ? "Lose" : "pending"}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                ))
              }
              {isPrevious &&
                prevPredictions.map((league) => (
                  <div key={league.league} className="mb-6">
                    <h2 className="text-sm capitalize text-white p-2">
                      <span className="font-bold  sm:text-base">
                        {league.league.split(":")[0]}:
                      </span>{" "}
                      {league.league.split(":")[1]}
                    </h2>

                    {/* Responsive Table */}
                    <div className="overflow-x-auto">
                      <table className="w-full mt-2 mb-2 text-xs sm:text-base border-separate border-spacing-0 min-w-[400px]">
                        <thead className="bg-gray-900 text-xs text-green-400">
                          <tr>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Time</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Match</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Prediction</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Odds</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">%</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Results</th>
                            <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Won</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-700">
                          {league.matches.map((match) => (
                            <tr
                              key={match.id}
                              className="cursor-pointer text-xs even:bg-gray-800 odd:bg-gray-700 text-white hover:bg-green-800 hover:text-black"
                              onClick={() => {
                                dispatch(setSelectedMatch(match));
                                navigate(`/predictions/${match.id}`);
                              }}
                            >
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.time}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.homeTeam} v {match.awayTeam}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.prediction}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.odds}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.chance}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">{match.result}</td>
                              <td className="px-3 py-2 sm:px-4 sm:py-3">
                                {match.won ? "Win" : match.result !== "-" ? "Lose" : "pending"}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                ))
              }
                 
          </div>
        </div>
        <div className="">
          <BestPick />
        </div>
      </div>
      <VIPBanner />
      <p className="p-4 text-xs text-center text-gray-400">
        {predictions.map((league) => league.league).join(", ")} predictions.  
        {predictions.map((league) => league.league).join(", ")} Both teams to score (BTTS).  
        {predictions.map((league) => league.league).join(", ")} over 2.5 sure predictions.  
        {predictions.map((league) => league.league).join(", ")} 100% sure predictions.
      </p>

      </div>
  );
};

export default Football;

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { fetchPredictions, setSelectedMatch } from "../redux/predictionsSlice";
import type { RootState, AppDispatch } from "../redux/store";
import Navbar from "~/components/navbar";
import VIPBanner from "~/components/banner";
import SureTipsAd from "~/components/notify";
import BetForm from "~/components/trackRecord";

const Football: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const predictions = useSelector((state: RootState) => state.predictions.data);
  const navigate = useNavigate();

  useEffect(() => {
    dispatch(fetchPredictions());
  }, [dispatch]);

  return (
    <div className="flex flex-col gap-2 pt-[25px] bg-gray-900 lg:px-[80px]">
      <Navbar />
      <div className="grid grid-cols-5 gap-4 w-full">
        <div className="flex flex-col gap-4">
          <SureTipsAd />
          <BetForm />
        </div>
        
        <div className="col-span-3">
        {predictions.map((league) => (
          <div key={league.league} className="mb-6">
            <h2 className="text-sm sm:text-2xl font-semibold text-white p-2">{league.league}</h2>

            {/* Responsive Table */}
            <div className="overflow-x-auto">
              <table className="w-full mt-2 mb-2 text-xs sm:text-base border-separate border-spacing-0 min-w-[400px]">
                <thead className="bg-gray-800 text-green-400">
                  <tr>
                    <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Time</th>
                    <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Match</th>
                    <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Prediction</th>
                    <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Odds</th>
                    <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">%</th>
                    <th className="px-3 py-2 sm:px-4 sm:py-3 text-left">Results</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-700">
                  {league.matches.map((match) => (
                    <tr
                      key={match.id}
                      className="cursor-pointer even:bg-gray-800 odd:bg-gray-700 text-white hover:bg-green-800 hover:text-black"
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
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <p className="p-4 text-xs text-center text-gray-400">
              {league.league} predictions. {league.league} Both teams to score (BTTS). {league.league} over 2.5 sure predictions. {league.league} 100% sure predictions.
            </p>
          </div>
        ))}
        </div>
        <div className="">
        Hello
        </div>
      </div>
      <VIPBanner />  
      </div>
  );
};

export default Football;

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { fetchPredictions, setSelectedMatch } from "../redux/predictionsSlice";
import type { RootState, AppDispatch } from "../redux/store";
import Navbar from "~/components/navbar";
import VIPBanner from "~/components/banner";

const Football: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const predictions = useSelector((state: RootState) => state.predictions.data);
  const navigate = useNavigate();

  useEffect(() => {
    dispatch(fetchPredictions());
  }, [dispatch]);
  

  return (
    <div className="flex flex-col gap-2 pt-[55px]">
      <Navbar />
      <div className="p-4">
        {predictions.map((league) => (
          <div key={league.league} className="mb-6">
            <h2 className="text-2xl font-semibold text-white p-2">{league.league}</h2>
            <table className="w-full mt-2 mb-2 border-separate border-spacing-0">
              <thead className="bg-gray-800 text-green-400">
                <tr>
                  <th className="px-4 py-3 text-left">Time</th>
                  <th className="px-4 py-3 text-left">Match</th>
                  <th className="px-4 py-3 text-left">Prediction</th>
                  <th className="px-4 py-3 text-left">Odds</th>
                  <th className="px-4 py-3 text-left">%</th>
                  <th className="px-4 py-3 text-left">Results</th>
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
                    <td className="px-4 py-3">{match.time}</td>
                    <td className="px-4 py-3">{match.homeTeam} v {match.awayTeam}</td>
                    <td className="px-4 py-3">{match.prediction}</td>
                    <td className="px-4 py-3">{match.odds}</td>
                    <td className="px-4 py-3">{match.chance}</td>
                    <td className="px-4 py-3">{match.result}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            <div className="flex mt-8">
              <VIPBanner />
              <div className="w-full"></div>
            </div>
            <p className="p-4 text-sm text-center text-gray-800">Get {league.league} predictions. {league.league} Both teams to score(btts). {league.league} over 2.5 sure predictions. {league.league} 100% sure predictions.</p>
          </div>
        ))}
      </div>

    </div>
  );
};

export default Football;

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { setPredictions, setSelectedMatch } from "../redux/predictionsSlice";
import type { RootState, AppDispatch } from "../redux/store";
import Navbar from "~/components/navbar";
import VIPBanner from "~/components/banner";

const Football: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const predictions = useSelector((state: RootState) => state.predictions.data);
  const navigate = useNavigate();

  // Force Adsense to appear
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

  useEffect(() => {
    const fetchPredictions = async () => {
      const sampleData = [
        {
          league: "Premier League",
          matches: [
            { id: 1, time: '9:00', homeTeam: "Manchester United", awayTeam: "Arsenal", prediction: "Draw", odds: "3.12", result: "-", reason: "Tactical balance expected.", chance: "82%"},
            { id: 2, time: '9:00', homeTeam: "Chelsea", awayTeam: "Liverpool", prediction: "Liverpool Win", odds: "3.12", result: "-", reason: "Liverpool's strong away form.", chance: "82%" },
          ],
        },
        {
          league: "La Liga",
          matches: [
            { id: 3, time:'9:00', homeTeam: "Real Madrid", awayTeam: "Barcelona", prediction: "Real Madrid Win", odds: "3.12", result: "-", reason: "Madrid's home advantage.", chance: "82%" },
            { id: 4, time: '9:00', homeTeam: "Atletico Madrid", awayTeam: "Sevilla", prediction: "Atletico Win", odds: "3.12", result: "-", reason: "Atletico's defensive strength.", chance: "82%" },
          ],
        },
      ];
      dispatch(setPredictions(sampleData));
    };

    fetchPredictions();
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

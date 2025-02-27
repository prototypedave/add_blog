import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { setPredictions, setSelectedMatch } from "../redux/predictionsSlice";
import type { RootState, AppDispatch } from "../redux/store";
import Navbar from "~/components/navbar";

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
            { id: 1, homeTeam: "Manchester United", awayTeam: "Arsenal", prediction: "Draw", odds: "3.12", result: "-", reason: "Tactical balance expected.", chance: "82%"},
            { id: 2, homeTeam: "Chelsea", awayTeam: "Liverpool", prediction: "Liverpool Win", odds: "3.12", result: "-", reason: "Liverpool's strong away form.", chance: "82%" },
          ],
        },
        {
          league: "La Liga",
          matches: [
            { id: 3, homeTeam: "Real Madrid", awayTeam: "Barcelona", prediction: "Real Madrid Win", odds: "3.12", result: "-", reason: "Madrid's home advantage.", chance: "82%" },
            { id: 4, homeTeam: "Atletico Madrid", awayTeam: "Sevilla", prediction: "Atletico Win", odds: "3.12", result: "-", reason: "Atletico's defensive strength.", chance: "82%" },
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
      <div className="flex gap-32 p-4 justify-center">
        <Link to="/football" className="active">Football</Link>
        <Link to="/basketball">Basketball</Link>
        <Link to="/ice-hockey">Ice Hockey</Link>
      </div>

      <div className="p-4">
        <h1 className="text-xl font-bold mb-4 text-center">Today's Football Predictions</h1>

        {predictions.map((league) => (
          <div key={league.league} className="mb-6">
            <h2 className="text-2xl font-semibold text-white p-2">{league.league}</h2>
            <table className="w-full mt-2">
              <thead className="bg-gray-200">
                <tr>
                  <th className="px-4 py-2">Match</th>
                  <th className="px-4 py-2">Prediction</th>
                  <th className="px-4 py-2">Odds</th>
                  <th className="px-4 py-2">%</th>
                  <th className="px-4 py-2">Results</th>
                </tr>
              </thead>
              <tbody>
                {league.matches.map((match) => (
                  <tr 
                    key={match.id} 
                    className="border cursor-pointer hover:bg-gray-100"
                    onClick={() => {
                      dispatch(setSelectedMatch(match));
                      navigate(`/predictions/${match.id}`);
                    }}
                  >
                    <td className="px-4 py-2">{match.homeTeam} v {match.awayTeam}</td>
                    <td className="px-4 py-2">{match.prediction}</td>
                    <td className="px-4 py-2">{match.odds}</td>
                    <td className="px-4 py-2">{match.chance}</td>
                    <td className="px-4 py-2">{match.result}</td>
                  </tr>
                ))}
              </tbody>
            </table>

            <div className="flex flex-col mt-4 bg-yellow-300 items-center text-center py-4">
              <p>Google Ad Placeholder</p>
              <p>Get well analyzed sure bets when you sign up for VIP.</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Football;

import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchMatches } from "../redux/bestSlice";
import type { RootState, AppDispatch } from "../redux/store";

const BestPick: React.FC = () => {
    const dispatch = useDispatch<AppDispatch>();
    const { data, loading, error } = useSelector((state: RootState) => state.matches);
  
    useEffect(() => {
      if (data.length === 0) {
        dispatch(fetchMatches());
      }
    }, [dispatch, data]);
  
    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;
  
    return (
      <div className="w-full bg-gray-800 shadow-lg relative">
        <h2 className="p-4 text-center font-semibold text-green-400">Todays Best Pick</h2>
        <div className="lg:border lg:border-gray-900 lg:mx-2"></div>
        <div className="p-2">
            <div className="flex justify-between text-xs text-yellow-400 p-2">
                <h3>ID</h3>
                <h3>TEAM</h3>
                <h3>PICK</h3>
                <h3>ODDS</h3>
            </div>
            <ol className="list-inside list-decimal text-xs p-2 flex flex-col gap-2">
                {data.map((league) => (
                    <div key={league.league}>
                        {league.matches.map((match) => (
                        <li key={match.id} className="flex justify-between">
                            <p>{match.id}</p>
                            <div className="flex flex-col">
                                <p>{match.homeTeam} <span>vs</span></p>
                                <p>{match.awayTeam}</p> 
                            </div>
                            <p>{match.prediction}</p> 
                            <p>{match.odds}</p>   
                        </li>
                    ))}
                    </div>
                ))}
                <p className="font-semibold mt-4 text-center text-yellow-400">
                    Total Odds: {data.flatMap(league => league.matches).reduce((acc, match) => acc * parseFloat(match.odds), 1).toFixed(2)}
                </p>
            </ol>
        </div>
                

      </div>
    );
  };
  
  export default BestPick;
  
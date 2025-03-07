import Navbar from "~/components/navbar";
import SureTipsAd from "~/components/notify";
import BetForm from "~/components/trackRecord";
import BestPick from "~/components/bestPicks";

const About: React.FC = () => {
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
                        <div className="flex text-sm py-2">
                            <h2>About Proto Predictz</h2>
                        </div>
                    </div>
                    <div className="lg:border lg:border-gray-900"></div>
                    <div className="">
                        <p>Proto Predictz utilizes the growing world of AI and machine learning to predict possible outcomes of the match, strengthen with diverse algorithm, Proto Predictz aim is to get 99% success rate in the predictions made.
                        </p>
                        <div className="">
                            <h3>Prediction Markets Made:</h3>
                            <h4>Over and Under Markets</h4>
                            <p>In football predictions, we are able to predict the possibility of a game ending in total 2.5 and total 3.5 markets, while on ice-hockey predictions are concentrated on the over 3.5 and 4.5 markets and for basketball any total is slected based on the possibiliy of that game ending to the given total.</p>
                            <h4>Team win</h4>
                            <p>Either side 'Home or Away win' is selected based on high confidence of a particular outcome</p>
                            <h4>Both Teams To Score</h4>
                            <p>Probablitly of teams facing each other to all score is analyzed and games with high confidence of BTTS making out is selected</p>
                        </div>
                        <div>
                            <p>Our model only provides possible outcomes and is not liable to any wrong prediction, You are advised to gamble responsibly</p>
                        </div>
                    </div>
                </div>
                <div className="">
                    <BestPick />
                </div>
            </div>
        </div>
    )
}

export default About
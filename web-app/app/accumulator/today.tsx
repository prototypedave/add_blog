import Navbar from "~/components/navbar";
import SureTipsAd from "~/components/notify";
import BetForm from "~/components/trackRecord";
import BestPick from "~/components/bestPicks";

const TodayBest: React.FC = () => {
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
                            <h2>Todays Best Bets</h2>
                        </div>
                    </div>
                    <div className="lg:border lg:border-gray-900"></div>
                    <div className="">
                        <p>Get todays best across all sports</p>
                        
                    </div>
                </div>
                <div className="">
                    <BestPick />
                </div>
            </div>
        </div>
    )
}

export default TodayBest
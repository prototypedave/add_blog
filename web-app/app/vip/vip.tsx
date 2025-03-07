import Navbar from "~/components/navbar";
import SureTipsAd from "~/components/notify";
import BetForm from "~/components/trackRecord";
import BestPick from "~/components/bestPicks";

const VIP: React.FC = () => {
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
                            <h2>VIP Betting Slips</h2>
                        </div>
                    </div>
                    <div className="lg:border lg:border-gray-900"></div>
                    <div className="">
                        <p>Maximize on your wins by subscribing today and get well crafted slips with higher chance of win</p>
                        <div className="">
                            <p>7 days for $2.99 <span><button>Subscribe</button></span></p>
                            <p>14 days for $4.99 <span><button>Subscribe</button></span></p>
                            <p>30 days for $11.99 <span><button>Subscribe</button></span></p>
                        </div>
                    </div>
                    <div className="lg:border lg:border-gray-900"></div>
                    <div className="">
                        <p>Sign in to your account</p>
                        <form>
                            <label>Email</label>
                            <input type="email" required/>
                            <label>Password</label>
                            <input type="password" />
                            <button>Sign In</button>
                        </form>
                        <p>Dont have an account yet? <button>Register</button></p>
                    </div>
                    <div className="">
                        <p>Subscribe to our VIP program</p>
                        <form>
                            <label>Email</label>
                            <input type="email" required/>
                            <label>Name:</label>
                            <input type="text" required />
                            <label>Subscription days</label>
                            <select required>
                                <option value={'7 days'}>7 days</option>
                                <option value={'14 days'}>14 days</option>
                                <option value={'30 days'}>30 days</option>
                            </select>
                            <label>Password</label>
                            <input type="password" />
                            <label>Confirm Password</label>
                            <input type="password" />
                            <button>Register</button>
                        </form>
                    </div>
                    <div className="lg:border lg:border-gray-900"></div>
                    <div className="">
                        <h3>Slip type</h3>
                        <div>day 5 <span></span></div>
                        <div>day 4 <span></span></div>
                        <div>day 3 <span></span></div>
                        <div>day 2 <span></span></div>
                        <div>day 1 <span></span></div>
                    </div>
                </div>
                <div className="">
                    <BestPick />
                </div>
            </div>
        </div>
    )
}

export default VIP
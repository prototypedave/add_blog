import Navbar from "~/components/navbar";
import SureTipsAd from "~/components/notify";
import BetForm from "~/components/trackRecord";
import BestPick from "~/components/bestPicks";

const Contact: React.FC = () => {
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
                            <h2>Contact Us</h2>
                        </div>
                    </div>
                    <div className="lg:border lg:border-gray-900"></div>
                    <div className="">
                        <p>To contact us please send email to popupgfj@gmail.com or use the form below.</p>
                        <form>
                            <label>Name</label>
                            <input type="text" required/>
                            <label>Email</label>
                            <input type="email" required />
                            <label>Message</label>
                            <textarea rows={4} />
                            <button>Send</button>
                        </form>
                    </div>
                </div>
                <div className="">
                    <BestPick />
                </div>
            </div>
        </div>
    )
}

export default Contact
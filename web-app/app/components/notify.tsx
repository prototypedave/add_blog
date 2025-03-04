export default function SureTipsAd() {
  const today = new Date().toISOString().split('T')[0];
  return (
    <div className="w-full bg-gray-800 shadow-lg relative">
        <div className="flex justify-between p-2 font-semibold text-green-400">
            <h2 className="p-2">VIP Tips</h2>
            <span className="bg-gray-900 p-2 rounded-lg">coming soon</span>
        </div>
        <div className="border border-gray-900 mx-2"></div>
        <div className="p-4 text-sm">
            <div className="flex gap-4">
                <div className="flex flex-col gap-1">
                    <p>Date:</p>
                    <p>Kick off:</p>
                    <p>Total odds:</p>
                </div>
                <div className="flex flex-col gap-1">
                    <span>{today}</span>
                    <span>19:45 UTC</span>
                    <span>4.39</span>
                </div>
            </div>
            <p className="my-2 font-semibold">Coming soon well analyzed bets</p>
            <div className="flex justify-center">
                <button className="p-2 bg-yellow-500 text-gray-900 font-semibold rounded-sm">Read More</button>
            </div>
            
        </div>
        
    </div>
  );
}

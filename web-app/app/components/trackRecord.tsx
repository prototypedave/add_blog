export default function BetForm() {
    const today = new Date().toISOString().split('T')[0];
    return (
      <div className="w-full bg-gray-800 shadow-lg relative">
          <div className="flex lg:justify-between justify-center p-2 font-semibold text-green-400">
              <h2 className="p-2">Slips Record</h2>
              <span className="bg-gray-900 p-2 rounded-lg">coming soon</span>
          </div>
          <div className="lg:border lg:border-gray-900 lg:mx-2"></div>
          
          {/* Mobile & Tablet*/}
          <div className="sm:block lg:hidden p-4 text-sm cursor-pointer flex justify-center items-center lg:bg-gray-700 text-white font-semibold rounded-md">
            <p className="my-2 font-semibold text-center">Want to maximize your win? Subscribe today to unlock sure tips and Accumulator tips that are well analyzed</p>
          </div>
          
          <div className="hidden lg:block p-4 text-sm">
              <p className="my-2 font-semibold">Betting tips form from our system</p>
              <div className="flex w-full text-xs">
                  <div className="flex flex-col gap-1 w-full">
                      <h3 className="text-center font-semibold py-2">Type</h3>
                      <p className="p-2 bg-gray-700 w-full">Sure Tips:</p>
                      <p className="p-2 ">Daily Tips:</p>
                      <p className="p-2 bg-gray-700">Best Tips:</p>
                  </div>
                  <div className="flex flex-col gap-1 w-full">
                      <h3 className="text-center font-semibold py-2">Form</h3>
                      <span className="p-2 bg-gray-700 text-right">1/1</span>
                      <span className="p-2 text-right">0/1</span>
                      <span className="p-2 bg-gray-700 text-right">0/1</span>
                  </div>
              </div>
              <p className="my-2 font-semibold">Want to maximize your win? Subscribe today to unlock sure tips and Accumulator tips that are well analyzed</p>
              <div className="flex justify-center">
                  <button className="p-2 bg-yellow-500 text-gray-900 font-semibold rounded-sm">Read More</button>
              </div>
              
          </div>
          
      </div>
    );
  }
  
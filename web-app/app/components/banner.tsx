import { useState } from "react";

export default function VIPBanner() {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <div className="relative w-full bg-gray-900 text-white py-8 px-6 flex flex-col md:flex-row items-center justify-between shadow-lg border-t-4 border-yellow-400">
      {/* Left Section - Text */}
      <div className="text-center md:text-left animate-fadeInLeft">
        <h2 className="text-2xl md:text-3xl font-bold text-yellow-400 animate-pulse">
          Join VIP & Win Big!
        </h2>
        <p className="text-gray-300 mt-2 md:mt-1 text-sm md:text-base">
          Get <span className="font-semibold text-yellow-300">exclusive betting tips, high-accuracy predictions, and premium odds!</span>
        </p>
      </div>

      {/* Right Section - Button */}
      <div className="mt-4 md:mt-0 transition-transform duration-300 transform scale-100 hover:scale-110">
        <button
          onMouseEnter={() => setIsHovered(true)}
          onMouseLeave={() => setIsHovered(false)}
          className={`bg-yellow-500 text-gray-900 px-6 py-2 rounded-full font-semibold text-lg shadow-lg transition-all duration-300 ${
            isHovered ? "scale-110" : "scale-100"
          }`}
        >
          Subscribe Now 🚀
        </button>
      </div>

      {/* Floating Badge */}
      <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-yellow-400 text-gray-900 px-4 py-1 rounded-full font-semibold text-sm shadow-md animate-bounce">
        Limited Offer!
      </div>
    </div>
  );
}

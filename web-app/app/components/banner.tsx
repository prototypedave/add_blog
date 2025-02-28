import { motion } from "framer-motion";

export default function VIPBanner() {
  return (
    <div className="relative w-full bg-gray-900 text-white py-8 px-6 flex flex-col md:flex-row items-center justify-between shadow-lg border-t-4 border-yellow-400">
      {/* Left Section - Text */}
      <motion.div
        initial={{ opacity: 0, x: -50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.8 }}
        className="text-center md:text-left"
      >
        <h2 className="text-2xl md:text-3xl font-bold text-yellow-400 animate-pulse">
          Join VIP & Win Big!
        </h2>
        <p className="text-gray-300 mt-2 md:mt-1 text-sm md:text-base">
          Get <span className="font-semibold text-yellow-300">exclusive betting tips, high-accuracy predictions, and premium odds!</span>
        </p>
      </motion.div>

      {/* Right Section - Button */}
      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.6, delay: 0.3 }}
        className="mt-4 md:mt-0"
      >
        <motion.button
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          className="bg-yellow-500 text-gray-900 px-6 py-2 rounded-full font-semibold text-lg shadow-lg hover:bg-yellow-400 transition duration-300"
        >
          Subscribe Now 🚀
        </motion.button>
      </motion.div>

      {/* Floating Badge */}
      <motion.div
        initial={{ y: -10 }}
        animate={{ y: 0 }}
        transition={{ repeat: Infinity, repeatType: "reverse", duration: 1 }}
        className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-yellow-400 text-gray-900 px-4 py-1 rounded-full font-semibold text-sm shadow-md"
      >
        Limited Offer!
      </motion.div>
    </div>
  );
}

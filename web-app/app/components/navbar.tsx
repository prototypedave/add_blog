import { useState } from "react";
import { Link } from "react-router-dom";
import { Menu, X } from "lucide-react"; 
import homeLogo from "./logo.svg";

const Navbar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="w-full bg-gray-900 text-green-400 shadow-lg px-4">
      <div className="flex flex-col lg:flex-row items-center justify-between sm:justify-start x">
        {/* Logo */}
        <Link to="/" className="flex items-center">
          <img src={homeLogo} alt="betting tips icon" className="h-[100px] sm:h-[100px] w-[100px] sm:w-[100px]" />
          <h1 className="py-4 px-2 text-yellow-400 text-2xl font-bold">PROTO PREDICTS</h1>
        </Link>
        
        <div className="flex text-sm items-center justify-between w-full lg:hidden text-green-400 hover:text-white focus:outline-none bg-gray-800 p-2">
          {/* Mobile Menu Button */}
          <h3 className="pl-2">Menu</h3>
          <button
            className=""
            onClick={() => setIsOpen(!isOpen)}
          >
            {isOpen ? <X size={18} /> : <Menu size={18} />}
          </button>
        </div>

        {/* Desktop Menu */}
        <div className="hidden lg:flex flex-1 justify-between lg:gap-4 space-x-4 p-6 ml-8">
          <NavLinks />
        </div>
      </div>

      {/* Mobile Dropdown */}
      {isOpen && (
        <div className="lg:hidden flex flex-col items-left text-white bg-gray-800 py-2">
          <NavLinks />
        </div>
      )}
    </nav>
  );
};

// Reusable NavLinks Component
const NavLinks: React.FC = () => (
  <>
    <Link to="/" className="hover:bg-gray-700 text-xs lg:hover:bg-transparent pl-4 px-4 py-2 lg:pl-0 lg:px-0  font-bold focus:text-white">FOOTBALL</Link>
    <Link to="/basketball" className="hover:bg-gray-700 text-xs pl-4 px-4 py-2 lg:pl-0 lg:px-0 lg:hover:bg-transparent py-2 font-bold focus:text-white">BASKETBALL</Link>
    <Link to="/ice-hockey" className="hover:bg-gray-700 text-xs pl-4 px-4 py-2 lg:pl-0 lg:px-0 lg:hover:bg-transparent py-2  font-bold focus:text-white">ICE-HOCKEY</Link>
    <Link to="/" className="hover:bg-gray-700 text-xs lg:hover:bg-transparent pl-4 px-4 py-2 lg:pl-0 lg:px-0 py-2  font-bold focus:text-white">TODAY'S BEST</Link>
    <Link to="/results" className="hover:bg-gray-700 text-xs pl-4 px-4 py-2 lg:pl-0 lg:px-0 lg:hover:bg-transparent py-2 font-bold focus:text-white">ABOUT</Link>
    <Link to="/vip" className="hover:bg-gray-700 text-xs pl-4 px-4 py-2 lg:pl-0 lg:px-0 lg:hover:bg-transparent py-2  font-bold focus:text-white">VIP</Link>
    <Link to="/vip" className="hover:bg-gray-700 text-xs pl-4 px-4 py-2 lg:pl-0 lg:px-0 lg:hover:bg-transparent py-2  font-bold focus:text-white">CONTACT US</Link>
  </>
);

export default Navbar;

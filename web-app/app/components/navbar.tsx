import { useState } from "react";
import { Link } from "react-router-dom";
import { Menu, X } from "lucide-react"; 
import homeLogo from "./logo.svg";

const Navbar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="w-full bg-gray-800 text-green-400 shadow-md">
      <div className="flex items-center justify-between sm:justify-start px-4">
        {/* Logo */}
        <Link to="/">
          <img src={homeLogo} alt="betting tips icon" className="h-[100px] sm:h-[100px] w-[100px] sm:w-[100px]" />
        </Link>
        <h1 className="py-4 px-2 text-yellow-400 text-2xl font-bold">PROTO PREDICTS</h1>

        {/* Mobile Menu Button */}
        <button
          className="sm:hidden text-green-400 hover:text-white focus:outline-none"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? <X size={28} /> : <Menu size={28} />}
        </button>

        {/* Desktop Menu */}
        <div className="hidden sm:flex flex-1 justify-between lg:gap-4 space-x-4">
          <NavLinks />
        </div>
      </div>

      {/* Mobile Dropdown */}
      {isOpen && (
        <div className="sm:hidden flex flex-col items-center bg-gray-900 py-2">
          <NavLinks />
        </div>
      )}
    </nav>
  );
};

// Reusable NavLinks Component
const NavLinks: React.FC = () => (
  <>
    <Link to="/" className="py-2 text-bs hover:text-white">Football</Link>
    <Link to="/basketball" className="py-2 text-base hover:text-white">Basketball</Link>
    <Link to="/ice-hockey" className="py-2 text-base hover:text-white">Ice Hockey</Link>
    <Link to="/" className="py-2 text-base hover:text-white">Accumulators</Link>
    <Link to="/results" className="py-2 text-base hover:text-white">Record</Link>
    <Link to="/vip" className="py-2 text-bs hover:text-white">VIP</Link>
  </>
);

export default Navbar;

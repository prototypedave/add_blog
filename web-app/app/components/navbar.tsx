import { useState } from "react";
import { Link } from "react-router-dom";
import { Menu, X } from "lucide-react"; // Install lucide-react for icons
import homeLogo from "./pred_logo.svg";

const Navbar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 w-full z-50 bg-gray-800 text-green-400 shadow-md">
      <div className="flex items-center justify-between px-4 py-3">
        {/* Logo */}
        <Link to="/">
          <img src={homeLogo} alt="betting tips icon" className="h-[40px] sm:h-[50px] w-[150px] sm:w-[200px]" />
        </Link>

        {/* Mobile Menu Button */}
        <button
          className="sm:hidden text-green-400 hover:text-white focus:outline-none"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? <X size={28} /> : <Menu size={28} />}
        </button>

        {/* Desktop Menu */}
        <div className="hidden sm:flex space-x-4">
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
    <Link to="/" className="py-2 text-lg hover:text-white">Football</Link>
    <Link to="/basketball" className="py-2 text-lg hover:text-white">Basketball</Link>
    <Link to="/ice-hockey" className="py-2 text-lg hover:text-white">Ice Hockey</Link>
    <Link to="/" className="py-2 text-lg hover:text-white">Accumulators</Link>
    <Link to="/results" className="py-2 text-lg hover:text-white">Record</Link>
    <Link to="/vip" className="py-2 text-lg hover:text-white">VIP</Link>
  </>
);

export default Navbar;

import { Link } from "react-router-dom";
import homeLogo from "./pred_logo.svg";

const Navbar: React.FC = () => {
  return (
    <nav className="fixed top-0 left-0 w-full z-50 flex flex-row w-full bg-gray-800 text-green-400  shadow-md">
        <Link to="/"> 
            <img src={homeLogo} alt="betting tips icon" className="h-[50px] w-[200px]" />
        </Link>
        <div className="flex flex-row w-full pl-2 items-center justify-around">
            <Link to="/" className="focus:text-white">Football</Link>
            <Link to="/basketball" className="focus:text-white">Basketball</Link>
            <Link to="/ice-hockey" className="focus:text-white">Ice Hockey</Link>
            <Link to="/" className="focus:text-white">Accumulators</Link>
            <Link to="/results" className="focus:text-white">Record</Link>
            <Link to="/vip" className="focus:text-white">VIP</Link>
        </div>
    </nav>
  );
};

export default Navbar;

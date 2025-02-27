import { Link } from "react-router-dom";
import homeLogo from "./pred_logo.svg";

const Navbar: React.FC = () => {
  return (
    <nav className="fixed top-0 left-0 w-full z-50 flex flex-row w-full bg-blue-200 shadow-md">
        <Link to="/"> 
            <img src={homeLogo} alt="betting tips icon" className="h-[50px] w-[200px]" />
        </Link>
        <div className="flex flex-row w-full pl-2 items-center justify-around">
            <Link to="/" className="active">Todays Predictions</Link>
            <Link to="/results" className="">Record</Link>
            <Link to="/stats" className="">Stats</Link>
            <Link to="/vip" className="">VIP</Link>
        </div>
    </nav>
  );
};

export default Navbar;

import type { Route } from "./+types/home";
import MatchDetails from "~/components/match";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Football Predictions | Latest Match Insights" },
    { name:"description", content:"Get expert predictions for football matches across all major leagues." },
  ];
}

export default function Home() {
  return <MatchDetails />;
}

import type { Route } from "./+types/home";
import Football from "../home/football";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Football Predictions | Latest Match Insights" },
    { name:"description", content:"Get expert predictions for football matches across all major leagues." },
  ];
}

export default function Home() {
  return <Football />;
}

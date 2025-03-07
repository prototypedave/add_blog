import TodayBest from "~/accumulator/today";
import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Football Predictions | Latest Match Insights" },
  ]
}

export default function Best() {
  return <TodayBest />;
}

import type { Route } from "./+types/home";
import About from "~/about/about";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Football Predictions | Latest Match Insights" },
  ]
}

export default function AboutUs() {
  return <About />;
}

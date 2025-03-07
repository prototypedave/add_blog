import type { Route } from "./+types/home";
import Hockey from "~/home/hockey";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Football Predictions | Latest Match Insights" },
    { name:"description", content:"Get expert predictions for football matches across all major leagues." },
    { name: "google-adsense-account", content:"ca-pub-1933580054760576"},
  ];
}

export default function Home() {
  return <Hockey />;
}

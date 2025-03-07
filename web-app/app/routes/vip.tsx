import VIP from "~/vip/vip";
import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Football Predictions | Latest Match Insights" },
    { name:"description", content:"Get expert predictions for football matches across all major leagues." },
    { name: "google-adsense-account", content:"ca-pub-1933580054760576"},
  ];
}

export default function Match() {
  return <VIP />;
}

import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
    index("routes/home.tsx"), 
    route("/predictions/:id", "routes/match.tsx"),
    route("/contact-us", "routes/contact.tsx"),
    route("/vip", "routes/vip.tsx"),
    route("/about", "routes/about.tsx"),
    route("/today/best", "routes/todays.tsx"),
    route("/ice-hockey", "routes/hockey.tsx"),
    route("/basketball", "routes/basket.tsx")
] satisfies RouteConfig;

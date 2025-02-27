import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [index("routes/home.tsx"), route("/predictions/:id", "routes/match.tsx")] satisfies RouteConfig;

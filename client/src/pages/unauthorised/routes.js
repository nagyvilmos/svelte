import Forgotton from "./Forgotton.svelte";
import Login from "./Login.svelte";

export const route = (router, setPage) =>
{
    router("/login", () => (setPage(Login)));
    router("/forgotton", () => (setPage(Forgotton)));
}
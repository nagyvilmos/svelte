import Authorised from "./Authorised.svelte";

export const route = (router, setPage) =>
{
    router("/home", () => (setPage(Authorised)));
}
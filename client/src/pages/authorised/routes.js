import Authorised from "./Authorised.svelte";
import ToDo from "./ToDo.svelte";

export const route = (router, setPage) =>
{
    router("/home", () => setPage(Authorised));
    router("/todo", () => {console.log("TODO"); setPage(ToDo);});
}
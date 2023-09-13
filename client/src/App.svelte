<script>
  import router from "page";
  import Root from "./pages/Root.svelte";
  import { auth } from "./store";
  import { route as routeUnauthorised } from "./pages/unauthorised/routes.js";
  import { route as routeAuthorised } from "./pages/authorised/routes.js";

  let loggedIn;

  let page;
  const setPage = (newPage) => {
    page = newPage;
  };

  routeUnauthorised(router, setPage);

  // this means the /home route MUST return the control to render.
  const authRoute = (route, routeFn) => {
    router(route, () => {
      const authedRoute = loggedIn
        ? !!routeFn
          ? routeFn()
          : "/home"
        : "/login";

        console.log({authedRoute})

        if (typeof authedRoute === "string") {
        router.redirect(authedRoute);
        return;
      }

      return authedRoute;
    });
  };
  routeAuthorised(authRoute, setPage);
  router("/*", () => {
    console.debug("...redirect");
    if (!loggedIn) {
      router.redirect("/login");
    } 
  });

  router.start();

  auth.subscribe((value) => {
    const wasLoggedIn = loggedIn;
    loggedIn = value.authorised;
    if (loggedIn && !wasLoggedIn) {
      router.redirect("/home");
    }
  });
</script>

<Root>
  <div slot="body">
    <svelte:component this={page} />
  </div>
</Root>

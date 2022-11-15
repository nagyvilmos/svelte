<script>
  import router  from "page";
  import Forgotton from "./Forgotton.svelte";
  import Login from "./Login.svelte";
  console.debug("...load unauthorised");

  let page;

  router("/login", () => (page = Login));
  router("/forgotton", () => (page = Forgotton));
  router("/*", () => {
    console.debug("...redirect");
    router.redirect("/login");
  });
  router.start();
</script>

<svelte:component this={page} />

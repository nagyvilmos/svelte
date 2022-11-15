<script>
  import router from "page";
  import Page from "./components/Page.svelte";
  import Fluid from "./components/raw/Fluid.svelte";
  import Header from "./components/Header.svelte";
  import Blog from "./spare/pages/Blog.svelte";
  import Index from "./spare/pages/Index.svelte";
  import Dashboard from "./spare/pages/Dashboard.svelte";
  import Phones from "./spare/pages/Phones.svelte";
  import Error from "./spare/pages/Error.svelte";
  import Responsive from "./spare/pages/Responsive.svelte";

  export let name;
  let page;

  router("/", () => (page = Index));
  router("/dashboard", () => (page = Dashboard));
  router("/phones", () => (page = Phones));
  router("/responsive", () => (page = Responsive));
  router("/blog", () => (page = Blog));
  router("*", () => (page = Error));

  router.start();
</script>

<main>
  <Fluid>
    <Page>
      <Header slot="header" {name} />
      <div slot="body">
        <h1>Vilmos {name}</h1>
        <p>
          <a href="/">home</a> |
          <a href="/dashboard">dashboard</a> |
          <a href="/phones">phone numbers</a> |
          <a href="/blog">blog</a> |
          <a href="/responsive">responsive</a>
        </p>
        <svelte:component this={page} {name} />    
      </div>
      <span slot="footer">Footer content @ today</span>
    </Page>
  </Fluid>
</main>

<!--
<style>
  :global(body) {
    font-size: 1vw;
  }
  :global(div) {
    font-size: 1vw;
  }
  :global(h1) {
    font-size: 3vw;
  }
  :global(h2) {
    font-size: 2.5vw;
  }
  :global(h3) {
    font-size: 2vw;
  }
  :global(h4) {
    font-size: 1.5vw;
  }

  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: calc(var(--fluid-3));
    font-weight: 150;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
-->

<script>
  import ThemeContext from "./ThemeContext.svelte";
  import Header from "./Header.svelte";
</script>

<ThemeContext>
  <div class="page">
    <div>
      <Header/>
      <article>
        <slot name="body">body</slot>
      </article>
    </div>
    <!-- End: Wrapper (Without footer) -->

    <footer class="footer secondary">
      <slot name="footer">footer</slot>
    </footer>
  </div>
</ThemeContext>

<style>
  .page {
    min-height: calc(100vh - 8px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: var(--theme-background);
    color: var(--theme-color);
  }
  .footer {
    border-top: 2pt;
  }
</style>

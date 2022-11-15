<script>
  import ToggleTheme from "./ToggleTheme.svelte";
  import { auth } from "../store";
  let loggedIn = false;
  auth.subscribe((value) => (loggedIn = value.authorised));
</script>

<header class="header primary">
  <h1 class="flex">
    <span>
      <slot name="header" />&nbsp;App
    </span>
    <span>
      {#if loggedIn}
        <button on:click={auth.logout}>Logout</button>
      {/if}
      <ToggleTheme />
    </span>
  </h1>
</header>

<style>
  .header {
    margin: 4px;
    border-radius: 12px;
  }
  button {
    background-color: var(--theme-background);
    color: var(--theme-color);
    border: 1px solid var(--theme-color);
    border-radius: 8px;
    margin: 4px;
    padding: 4px;
  }
  .flex {
    display: flex;
    justify-content: space-between;
  }
</style>

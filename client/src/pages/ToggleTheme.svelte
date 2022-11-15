<script>
  import { settings } from "../store";
  let theme = "-";
  settings.subscribe((settings) => (theme = settings.theme.current));
</script>

<button on:click={settings.toggleTheme}>{theme}</button>

<style>
  button {
    background: var(--theme-background);
    color: var(--theme-color);
    border: 1px solid var(--theme-color);
    margin: 4px;
    padding: 4px;
    border-radius: 8px;
  }
</style>

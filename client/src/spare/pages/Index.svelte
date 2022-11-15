<script>
    import Box from "../../components/Box.svelte";
    import Random from "../../components/Random.svelte";

    export let name = "World"
</script>

<Box background="lightgreen" width="512px">
    <h1>Szervusz {name}!</h1>
    <p>
      Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
      how to build Svelte apps.
    </p>
</Box>
<Random />

<style>
    h1 {
      color: #ff3e00;
      text-transform: uppercase;
      font-weight: 200;
    }
</style>
  
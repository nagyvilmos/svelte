<script>
  import Box from "./Box.svelte";
  import Markdown from "./Markdown.svelte";
  let rand = "not set";
  function getRand() {
    fetch("./api/rand")
      .then((d) => d.text())
      .then((d) => (rand = d));
  }
</script>

<Box>
    <p>Your number is {rand}!</p>

    <button on:click={() => getRand()}>Get a random number</button>
</Box>

<Markdown body="test this"/>

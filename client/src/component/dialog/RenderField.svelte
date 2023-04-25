<script>
  import Text from "./field/Text.svelte";
  import Label from "./field/Label.svelte";
  import Button from "./field/Button.svelte";

  export let body;

  const {type, ...props} = body;
  const Field = {
    text: Text,
    button: Button,
    label: Label,
  }[type]
</script>

{#if !!Field}
    <Field {...props} />
{:else}
    <span>[Unknown field - {type}]</span>
{/if}


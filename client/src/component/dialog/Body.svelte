<script>
    import RenderField from "./RenderField.svelte";
    export let layout;
</script>

{#if !layout || !layout.body}
    <p>MISSING BODY</p>
{:else}
    {#each layout.body as child}
        <RenderField body={child} />       
    {/each}
{/if}
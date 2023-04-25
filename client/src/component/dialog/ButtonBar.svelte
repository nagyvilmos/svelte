<script>
    import Button from "./field/Button.svelte";
    export let buttons;
</script>

<div class="buttonBar">
{#each buttons as child}
    <Button {...child} />       
{/each}
</div>
<style>
    .buttonBar {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
        gap: 8px;
    }
</style>
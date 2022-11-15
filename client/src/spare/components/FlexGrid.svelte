<script>
    export let container="flex-start";
    export let wrap="wrap";
</script>

<div class="grid" style="--container:{container};--wrap:{wrap};">
  <slot />
</div>

<style>
    .grid {
        display: flex;
        flex-wrap: var(--wrap);
        justify-content: var(--container);
    }

</style>
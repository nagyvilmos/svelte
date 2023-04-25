<script>
    export let style = "positive";
    export let disabled = false;
    export let type;
    export let label;
</script>

<button class={style} disabled={disabled} type={type}>{label}</button>

<style>
    button {
        border-radius: 8px;
        width:fit-content;
        display: inline;
    }
</style>
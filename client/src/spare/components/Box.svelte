<script>
    export let width = "50%";
	export let background = "lightblue";
    export let container = null;
    export let content = false;
</script>

<div
    class="box"
    class:container
    class:content
    style="--background:{background};--width:{width};--container:{container};"
>
	<slot></slot>
</div>

<style>
	.box {
        background-color: var(--background);
        width: var(--width);
        border: 1px solid #aaa;
		border-radius: 8px;
		box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
		padding: 1em;
		margin: 4px;
        align-self: center;
	}
    .container {
        display: flex;
        justify-content: var(--container);
    }
    .content {
        flex: auto,
    }
</style>
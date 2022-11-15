<script>
    export let size = 3;
    export let width = undefined;
    export let background = "red";

    const getWidth = () => {
        let widthStr = width || `${size*8}%`;
        console.debug({size, width, widthStr});
        return widthStr
    } 
</script>

<div
    class="content"
    style="--width:{getWidth()}; --background:{background};"
    on:click
>
    <slot></slot>
</div>

<style>
    .content {
        width: var(--width);
        background-color: var(--background);
        border: 1px solid #aaa;
		border-radius: 8px;
		box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
		padding: 8px 4px;
		margin: 4px;
        align-self: center;
    }
</style>
<script>
    import Box from "./Box.svelte";
    import Container from "./Container.svelte";

    export let name = "Test"
 </script>

<Box container="space-between" width="100cw" background="lightgrey">
    <Container size=4 background="darkgrey">
        <span>{name}</span>
        <span>Y</span>
    </Container>
    <Container size=2 background="darkgrey">
        <span>Z</span>
    </Container>
</Box>
<!--
<div class="header">
    <div class="item">
        <span>X</span>
        <span>Y</span>
    </div>
    <div class="item">
        <span>Z</span>
    </div>
</div>

<style>
	.header {
        color: lightcyan;
        background-color: teal;
        border: 1px solid #aaa;
		box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
		padding: 1em;
		margin: 0 2px 4px 2px;
        display: flex;
        justify-content: space-between;
	}
    .item {
        flex: content,
    }
</style>
-->
<script>
    export let body = "";
    import parser from "./markdownParser";
</script>

<div>
    {@html parser(body)}
</div>
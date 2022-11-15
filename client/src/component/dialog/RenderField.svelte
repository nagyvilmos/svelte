<script>
    export let body;

    const getField = (type) => ({
        text: TextField
    }[type] ?? LabelField)
</script>


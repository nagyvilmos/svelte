<script>
    export let value;
    export let label;
    export let prompt;
    export let format = "text";
    export let style = "base";
</script>

<div class={`${style} textOnInput`}>
    {#if !!value && !!label}<label for="inputText">{label}</label>{/if}
    {#if format === "text"}
        <input class={`${style} form-control`} type="text" bind:value={value} placeholder={prompt || label || ""}>
    {:else if format === "password"}
        <input class={`${style} form-control`} type="password" bind:value={value} placeholder={prompt || label || "" }>
    {:else}
        <span>[Unknown text format - {format}]</span>
    {/if} 
</div>

 <style>
    .textOnInput {
        position: relative;
    }
    .textOnInput label {
        position: absolute;
        background-color: inherit;
        top: -16px;
        left: 16px;
        padding: 2px;
        z-index: 1;
    }
    .textOnInput label:after {
        content: " ";
        width: 100%;
        height: 13px;
        position: absolute;
        left: 0;
        bottom: 0;
        z-index: -1;
    }
    label {
        font-size: 16px;
        font-weight: 500;
        display: inline-block;
        margin-bottom: .5rem;
    }
    .form-control {
        box-shadow: none !important;
        border: 2px solid;
        border-radius: 8px;
        margin-left: auto;
        margin-right: auto;
        width: 20vw;
        padding: 4px;
    }
    </style>

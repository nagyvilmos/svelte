<script>
    import Body from "./Body.svelte";
    import ButtonBar from "./ButtonBar.svelte";
    export let layout;
    let buttons = [{name:"cancel", label: "Cancel", style:"negative-reverse"}]
    $: if (!!layout?.buttons)
    {
        if (layout.buttons.find(b => b.name === "cancel"))
        {
            buttons = layout.buttons;
        }
        else
        {
            buttons = [buttons, layout.buttons].flat();
        }

        const lastButton = buttons.length-1;
        buttons.forEach((b,i) => {
            if (!b.style)
            {
                b.style = i === lastButton ? "positive" : "positive-reverse"
            }
        })
        console.debug({buttons})
    }
</script>

<div class="form">
<Body layout={layout} />
<ButtonBar buttons={buttons} />
</div>

<style>
    .form {
        width: fit-content;
    }
</style>
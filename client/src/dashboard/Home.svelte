<script>
  import Dialog from "../component/dialog/Dialog.svelte";
  let current = undefined;
  let randoms = ["Lorum", "Ipsum", "Carpe", "Dium"];
  let views = randoms.map((r, i) => ({
    name: r,
    index: i,
    modules: randoms
      .filter((m) => m !== r)
      .map((m, j) => {
        const total = Math.floor(Math.random() * 10);
        return {
          name: m,
          index: j,
          count: Math.floor(Math.random() * total + 1),
          total,
        };
      }),
  }));

  const selectModule = (view, module, offset = -1) => {
    const vI = views.findIndex((v) => v.index === view);
    const mI = views[vI].modules.findIndex((m) => m.index === module);
    if (offset === 0) {
      views[vI].modules[mI].count = 0;
      return;
    }
    const count = views[vI].modules[mI].count;
    if (count > 0 || offset > 0) {
      views[vI].modules[mI].count = count + offset;
    }
    if (offset > 0) {
      views[vI].modules[mI].total = views[vI].modules[mI].total + offset;
    }
  };
  const maxCount = (modules) => Math.max(...modules.map((m) => m.count));
  const sumModule = (modules, field) =>
    modules.map((m) => m[field]).reduce((a, b) => a + b, 0);
  const selectView = (select) => {
    current = select !== current ? select : undefined;
  };

  const getClass = (count) =>
    count > 7
      ? "collapsed urgent"
      : count > 4
      ? "collapsed pending"
      : count > 0
      ? "collapsed active"
      : "collapsed none";
</script>

<Dialog layout={{
  body: [{type:"text", label: "Email", prompt: "Enter email"}
  ,{type:"text", format:"password", label: "Password", password:"*"}],
  buttons:[{name:"woop", label: "PRESS ME"}]
}}/>

<div on:click={() => selectView()}>
  {#each views.sort( (a, b) => (a.index === current ? 1 : b.index === current ? -1 : a.index - b.index) ) as view}
    <div
      class={view.index === current
        ? "selected"
        : getClass(maxCount(view.modules))}
      on:click|stopPropagation={() => selectView(view.index)}
    >
      {#if view.index === current}
        <h1 class="content">{view.name}</h1>
        {#each view.modules as module}
          <div
            class={getClass(module.count)}
            on:click|stopPropagation={() =>
              selectModule(view.index, module.index)}
          >
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <h4
              class="content"
              on:click|stopPropagation={() =>
                selectModule(view.index, module.index, 1)}
            >
              {module.name}
            </h4>
            <p
              class="content"
              on:click|stopPropagation={() =>
                selectModule(view.index, module.index, 0)}
            >
              {module.count} / {module.total}
            </p>
          </div>
        {/each}
        {/if}
        <!-- {:else} -->
        <h4 class="content">{view.name}</h4>
        <p class="content">
          {sumModule(view.modules, "count")} / {sumModule(
            view.modules,
            "total"
          )}
        </p>
      <!-- {/if} -->
    </div>
  {/each}
</div>

<style>
  .content {
    border: 1px solid;
    border-radius: 6px;
    padding: 2px;
    opacity: 1;
  }
  .urgent {
    background-color: var(--theme-error);
  }
  .pending {
    background-color: var(--theme-warning);
  }
  .active {
    background-color: var(--theme-info);
  }
  .none {
    background-color: var(--theme-secondary);
  }
  .collapsed {
    display: inline-block;
    width: 64px;
    height: 128px;
    border: 1px solid grey;
    border-radius: 8px;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
    padding: 8px 4px;
    margin: 4px;
    align-self: center;
  }
  .collapsed:hover {
    opacity: 0.5;
  }
  .selected {
    background-color: #ccf;
    min-width: 128px;
    min-height: 256px;
    border: 1px solid #cfc;
    border-radius: 8px;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
    padding: 12px 12px;
    margin: 4px;
    align-self: center;
  }
</style>

<script>
  import Container from "../../components/Container.svelte";
  import FlexGrid from "../../components/FlexGrid.svelte";

  const tabs = [
    { id: "a", name: "Aaa" },
    { id: "b", name: "Bb" },
    { id: "c", name: "C Ccc" },
  ];
  const options = [
    { id: 1, group: "a", name: "aa aa" },
    { id: 2, group: "a", name: "aa bb" },
    { id: 3, group: "a", name: "aa cc" },
    { id: 4, group: "a", name: "aa dd" },
    { id: 11, group: "b", name: "bb aa" },
    { id: 12, group: "b", name: "bb bb" },
    { id: 13, group: "b", name: "bb cc" },
    { id: 14, group: "b", name: "bb dd" },
    { id: 15, group: "b", name: "bb ee" },
    { id: 21, group: "c", name: "cc aa" },
    { id: 22, group: "c", name: "cc bb" },
    { id: 23, group: "c", name: "cc cc" },
  ];

  let selectedTab = "a";
  let mru = [];

  const select = (id) => {
    mru = [id, ...mru.filter((x) => x !== id)].slice(0, 3);
    console.debug({mru});
  };
</script>

<div>
  {#if mru.length>0}
    <FlexGrid>
      {#each mru
        .map(m => options.find(op => op.id === m)) as item
      }
        <Container
        size={3}
        on:click={() => {
          console.log({item});
          select(item.id);
        }}
        >
            {item.name}
        </Container>
      {/each}
    </FlexGrid>
  {/if}
  <FlexGrid>
        {#each tabs as tab}
      <Container
        background={tab.id === selectedTab ? "blue" : "yellow"}
        size={2}
        on:click={() => {
          console.log({tab});
          selectedTab = tab.id;
        }}
      >
        {tab.name}
      </Container>
    {/each}
  </FlexGrid>

  <FlexGrid>
    {#each options.filter(op => op.group === selectedTab) as item
    }
      <Container
      size={3}
      background="lightgreen"
      on:click={() => {
        console.log({item});
        select(item.id);
      }}
      >
          {item.name}
      </Container>
    {/each}
  </FlexGrid>

</div>

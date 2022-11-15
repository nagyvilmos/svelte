<script>
  	import { onMount } from 'svelte';
    export let fluid = {};

    const defaults = {
        "min-width": 320,
        "max-width": 1500,
        "min-size": 8,
        "max-size": 16,
        "min-ratio": 1.2,
        "max-ratio": 1.5,
    };

    onMount(() => {
    Object.keys(defaults).forEach(key => {
        const value = fluid[key] ?? defaults[key];
        document.documentElement.style.setProperty(`--fluid-${key}`, value);
    });
    });
</script>


<slot />

<style>
:root {
  --fluid-screen: 100vw;
  --fluid-bp: calc((var(--fluid-screen) - ((var(--fluid-min-width) / 16) * 1rem)) / ((var(--fluid-max-width) / 16) - (var(--fluid-min-width) / 16)));
}

@media screen and (min-width: 1500px) {
  :root {
    --fluid-screen: calc(var(--fluid-max-width) * 1px);
  }
}

:root {
  --fluid-min-scale-0: var(--fluid-min-ratio);
  --fluid-min-scale-1: var(--fluid-min-scale-0) * var(--fluid-min-ratio);
  --fluid-min-scale-2: var(--fluid-min-scale-1) * var(--fluid-min-ratio);
  --fluid-min-scale-3: var(--fluid-min-scale-2) * var(--fluid-min-ratio);
  --fluid-min-scale-4: var(--fluid-min-scale-3) * var(--fluid-min-ratio);

  --fluid-max-scale-0: var(--fluid-max-ratio);
  --fluid-max-scale-1: var(--fluid-max-scale-0) * var(--fluid-max-ratio);
  --fluid-max-scale-2: var(--fluid-max-scale-1) * var(--fluid-max-ratio);
  --fluid-max-scale-3: var(--fluid-max-scale-2) * var(--fluid-max-ratio);
  --fluid-max-scale-4: var(--fluid-max-scale-3) * var(--fluid-max-ratio);

  --fluid-min-size-0: (var(--fluid-min-size)) / 16;
  --fluid-min-size-1: (var(--fluid-min-size) * var(--fluid-min-scale-0)) / 16;
  --fluid-min-size-2: (var(--fluid-min-size) * var(--fluid-min-scale-1)) / 16;
  --fluid-min-size-3: (var(--fluid-min-size) * var(--fluid-min-scale-2)) / 16;
  --fluid-min-size-4: (var(--fluid-min-size) * var(--fluid-min-scale-3)) / 16;

  --fluid-max-size-0: (var(--fluid-max-size)) / 16;
  --fluid-max-size-1: (var(--fluid-max-size) * var(--fluid-max-scale-0)) / 16;
  --fluid-max-size-2: (var(--fluid-max-size) * var(--fluid-max-scale-1)) / 16;
  --fluid-max-size-3: (var(--fluid-max-size) * var(--fluid-max-scale-2)) / 16;
  --fluid-max-size-4: (var(--fluid-max-size) * var(--fluid-max-scale-3)) / 16;

  --fluid-0: calc(((var(--fluid-min-size-0) * 1rem) + (var(--fluid-max-size-0) - var(--fluid-min-size-0)) * var(--fluid-bp)));
  --fluid-1: calc(((var(--fluid-min-size-1) * 1rem) + (var(--fluid-max-size-1) - var(--fluid-min-size-1)) * var(--fluid-bp)));
  --fluid-2: calc(((var(--fluid-min-size-2) * 1rem) + (var(--fluid-max-size-2) - var(--fluid-min-size-2)) * var(--fluid-bp)));
  --fluid-3: calc(((var(--fluid-min-size-3) * 1rem) + (var(--fluid-max-size-3) - var(--fluid-min-size-3)) * var(--fluid-bp)));
  --fluid-4: calc(((var(--fluid-min-size-4) * 1rem) + (var(--fluid-max-size-4) - var(--fluid-min-size-4)) * var(--fluid-bp)));
}

:global(body) {
  font-size: var(--fluid-0);
}
:global(div) {
  font-size: var(--fluid-0);
}
:global(span) {
  font-size: var(--fluid-0);
}
:global(h1) {
  font-size: var(--fluid-4);
}
:global(h2) {
  font-size: var(--fluid-3);
}
:global(h3) {
  font-size: var(--fluid-2);
  font-weight: bold;
}
:global(h4) {
  font-size: var(--fluid-2);
  font-weight: normal;
}
</style>
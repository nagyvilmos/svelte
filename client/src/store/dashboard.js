import { writable, derived  } from 'svelte/store';

const createDashboard = () => {
	const { subscribe, update} = writable({
        dashboards: [
            {
                id: "test",
                name: "Test This"
            },
            {
                id: "second",
                name: "Second"
            },
        ],
        current: undefined,
    });

	return {
		subscribe,
        setCurrent:(current) => update(n => ({...n, current}))
	};
};
const dashboard = createDashboard();
const currentDashboard = derived(dashboard,
    $dashboard => dashboard.current
);

export {dashboard, currentDashboard}
import { writable } from 'svelte/store';

export default (name, initialValue, onLoad, onSave) => {
    const value = window.localStorage.getItem(name);
    const passThrough = (x,y) => x;
    const loadFunc = onLoad ?? passThrough;
    const saveFunc = onSave ?? passThrough;
    const createValue = !!value ? JSON.parse(value) : initialValue; 
    const { subscribe, set, update} = writable(loadFunc(createValue));

    subscribe((value) => {
        window.localStorage.setItem(name, JSON.stringify(
            saveFunc(value)));
    });

    return {
        subscribe,
        set,
        update
    }
}
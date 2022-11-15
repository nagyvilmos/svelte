import persisted from './persisted';
import { themes } from "./themes.js";

const availableThemes = Object.keys(themes);
const defaultTheme = availableThemes[0];

const onLoad = (settings) => {
	const {theme} = settings;
	return {
		...settings,
		theme: {
			names: availableThemes,
			current: availableThemes.includes(theme.current) ? theme.current : defaultTheme,
			available:themes
		}
	}
}

const createSettings = () => {
	const { subscribe, update} = persisted("settings",{},onLoad);

	return {
		subscribe,
		toggleTheme:() => {
			update(values => {
				const names = values?.theme?.names;
				if (!names)
				{
					return values
				}
				let pos = names.indexOf(values.theme.current);
				let name = pos < names.length-1
					? names[pos+1]
					: names[0];

				return {
					...values,
					theme: {
						names: availableThemes,
						current: name,
						available:themes
					}
				}
			})
		},
	};
};

export const settings = createSettings();

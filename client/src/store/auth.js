import persisted from './persisted';
import router from "page";

const createAuth = () => {
	const { subscribe, set} = persisted("auth",{user:undefined,authorised:false});

	return {
		subscribe,
		login: (settings) => {
            set(settings); 
        },
		logout: () => {
			set({user:undefined,authorised:false});
			router.show("/logout")
		},
	};
};

export const auth = createAuth();

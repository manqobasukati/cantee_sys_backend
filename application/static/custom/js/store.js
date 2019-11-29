var store = new Vuex.Store({
	state:{
		input_surname:'',
		server_url:'http://127.0.0.1:5000/spa/api/surnames',
		search_results:[
			{id:0,surname:'Dlamini',praise_name:'Nkhosi Gwalagwalas',relations:['Nkhosi','Mlangeni'],are_you:true},
				{id:1,surname:'Sukati',praise_name:'Msime Lomnyama wasegodlwayo',relations:['Msime','Mbonane'],are_you:true},
		]
	},
	mutations:{
		SEARCH_SURNAME(state,payload){
			state.input_surname = payload;
		},
		async LOAD_SURNAMES_FROM_SERVER(state){
			console.log("info from server loaded...");
			state.search_results = await load_all_surnames_from_server(state.server_url);
			console.log(state.search_results);			
		}
	},
	actions:{
		SEARCH_SURNAME_ACTION(state, payload){
			state.commit('SEARCH_SURNAME', payload)
		},
		LOAD_SURNAMES_FROM_SERVER_ACTION(state){
			state.commit('LOAD_SURNAMES_FROM_SERVER');
		}
	},
	getters:{
		getSearchInput( state ){
			return state.input_surname;
		},
		getAllSurnames( state ){
			return state.search_results;
		},
		getSurname( state){
			let result;
			//console.log(payload);
			//console.log(state.search_results[0]);
			/*
			for(var i=0;i<=state.search_results.length;i++){
				if(state.search_results[i].id === payload){
					result = state.search_results[i];
				}
			}
			*/
			return result;
			
		}
	}
})

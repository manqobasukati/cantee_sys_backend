
const router = new VueRouter({
	routes:[
	{ path:'/', component:HomePage},
	{ path:'/home', component:HomePage},
	{ path:'/stats', component:StatsPage},
	{ path:'/about', component:AboutPage},
	{ 
		path:'/surname/:user_id',
		name:'SurnamePage',
		component:SurnamePage,
		props: true
	}
	]
});
	


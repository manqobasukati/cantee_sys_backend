//server hander

async function load_all_surnames_from_server(url){
	let surnames;
	self  = this;
	await fetch(url)
		.then(function(response) {
			return response.json();
		   })
		.then((myJson)=>{
		
			self.surnames = myJson;
		});
				
	console.log(self.surnames);
	return self.surnames;
}

def return_as_dict(db_obj):
	my_dict = db_obj.__dict__
	if '_sa_instance_state' in my_dict:
		del my_dict['_sa_instance_state']
	
	return my_dict


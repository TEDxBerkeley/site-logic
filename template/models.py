from logic.v1.models import Document, db


class Sample(Document):
	"""
	Models are defined using Flask-Mongoengine. For all options, see
	flask-mongoengine.readthedocs.org or mongoengine.readthedocs.org
	
	*Note*: If parameters here have required=True and args are auto-generated
	using model.fields_to_args(), the API will require that parameter in the 
	API call.
	
	To ameliorate the API issue, you have one of two options:
	- override options:
		model.fields_to_args(override={'required': False})
	- override the argument:
		model.fields_to_args(required=Arg(str, required=False))
	"""
	
	options = ['a', 'b', 'c', 'd']
	
	option = db.StringField(choices=options)
	required = db.IntField(default=10, required=True)
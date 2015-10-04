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


class Speaker(Document):
    """  Speaker class -  """
    name = db.StringField(max_length=255, required=True)
    tagline = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    status = db.StringField(default="UnderReview", required=True)

class Nomination(Document):
    """ Nomination class - Must be connected to a speaker object """
    speaker = db.ReferenceField(Speaker)
    nominator_email = db.StringField(max_length=255, required=True)
    nominator_name = db.StringField(max_length=255, required=True)
    speaker_pitch = db.StringField(required=True)

class Conference(Document):
    """ Conference class - Describes TEDxBerkeley[year] """
    year = db.IntField(required=True)
    theme = db.StringField(required=True)
    speakers = db.EmbeddedDocumentField(Speaker) #Does this make sense to do with a List Field instead? Not totally sure how to do many to one relationships best in Mongo.



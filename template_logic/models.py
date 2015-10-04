from logic.v1.models import Document, db


class Speaker(Document):
    """  Speaker class -  """
    statuses = ['pending review', 'under review', 'accepted', 'declined']
    name = db.StringField(max_length=255, required=True)
    tagline = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    status = db.StringField(default="pending review", required=True, choices=statuses)
    avatar = db.StringField() # path to image
    conference = db.ReferenceField()


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


class Engagements(Document):
    """ Engagements class - Connects speaker to conference """
    conference = db.ReferenceField(Conference)
    speaker = db.ReferenceField(Speaker)

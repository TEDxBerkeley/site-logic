from logic.v1.models import Document, db


class Conference(Document):
    """ Conference class - Describes TEDxBerkeley[year] """
    year = db.IntField(required=True)
    theme = db.StringField(required=True)


class Speaker(Document):
    """  Speaker class -  """
    statuses = ['pending review', 'under review', 'accepted', 'declined']
    name = db.StringField(max_length=255, required=True)
    tagline = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    status = db.StringField(default="pending review", required=True, choices=statuses)
    avatar = db.StringField() # path to image
    conference = db.ReferenceField(Conference)


class Staff(Document):
    """ Staff class """
    name = db.StringField(max_length = 225, required = True)
    tagline = db.StringField(max_length = 225, required = True)
    description = db.StringField(required = True)
    avatar = db.StringField() #path to image


class Nomination(Document):
    """ Nomination class - Must be connected to a speaker object """
    speaker = db.ReferenceField(Speaker)
    nominator_email = db.StringField(max_length=255, required=True)
    nominator_name = db.StringField(max_length=255, required=True)
    speaker_pitch = db.StringField(required=True)


class Engagement(Document):
    """ Engagements class - Connects speaker to conference """
    conference = db.ReferenceField(Conference)
    speaker = db.ReferenceField(Speaker)


class Membership(Document):
    """ Membership class - Connects staff to conference """
    staff = db.ReferenceField(Staff)
    conference = db.ReferenceField(Conference)

from logic.v1.api import BaseAPI, need, hook
from logic.v1.args import KeyArg, Arg
from logic.v1.core.models import User
from . import models


class SpeakerAPI(BaseAPI):
    model = models.Speaker

    methods = {
        'get': {
            'args': model.fields_to_args(override={'required': False})
        },
        'post': {
            'args': model.fields_to_args(
                conference=KeyArg(models.Conference))
        },
        'put': {
            'args': model.fields_to_args()
        },
        'delete': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    endpoints = {
        'fetch': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    def pre_post(self, obj, data, _):
        """Temporarily save conference to obj"""
        self.conference = data.pop('conference', None).get()

    def post_post(self, obj, data, rval):
        """Properly links speaker to conference"""
        if self.conference:
            models.Engagement(conference=self.conference,
                speaker=rval.id).post()

    def post_delete(self, obj, data, rval):
        """Removes all associated Engagement objects and Nominations"""
        for eng in models.Engagement(speaker=obj.id).fetch():
            eng.delete()
        for nom in models.Nomination(speaker=obj.id).fetch():
            nom.delete()

    def can(self, obj, user, permission):
        """Returns a boolean allowing or denying API access"""
        if permission in ['post', 'get', 'put', 'delete', 'fetch']:
            return True
        return False


class NominationAPI(BaseAPI):
    model = models.Nomination

    methods = {
        'get': {
            'args': model.fields_to_args(override={'required': False})
        },
        'post': {
            'args': model.fields_to_args()
        },
        'put': {
            'args': model.fields_to_args()
        },
        'delete': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    endpoints = {
        'fetch': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    def can(self, obj, user, permission):
        """Returns a boolean allowing or denying API access"""
        if permission in ['post', 'get', 'put', 'delete', 'fetch']:
            return True
        return False


class ConferenceAPI(BaseAPI):
    model = models.Conference

    methods = {
        'get': {
            'args': model.fields_to_args(override={'required': False})
        },
        'post': {
            'args': model.fields_to_args()
        },
        'put': {
            'args': model.fields_to_args()
        }
    }

    endpoints = {
        'fetch_speakers': {},
        'fetch_staff': {},
        'get_or_create': {
            'args': model.fields_to_args(override={'required': False})
        },
        'fetch': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    def fetch_staff(self, obj, user):
        """Fetches list of all staff members"""
        members = models.Membership(conference=obj).fetch()
        return [member.staff for member in members]

    def fetch_speakers(self, obj, user):
        """Fetches list of all speakers"""
        engagements = models.Engagement(conference=obj).fetch()
        return [engagement.speaker for engagement in engagements]

    def can(self, obj, user, permission):
        """Returns a boolean allowing or denying API access"""
        if permission in ['post', 'get', 'put', 'delete', 'fetch']:
            return True
        return False


class EngagementAPI(BaseAPI):
    model = models.Engagement

    methods = {
        'get': {
            'args': model.fields_to_args(override={'required': False})
        },
        'post': {
            'args': model.fields_to_args()
        },
        'put': {
            'args': model.fields_to_args()
        },
        'delete': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    endpoints = {
        'fetch': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    def can(self, obj, user, permission):
        """Returns a boolean allowing or denying API access"""
        if permission in ['post', 'get', 'put', 'delete', 'fetch']:
            return True
        return False


class StaffAPI(BaseAPI):
    model = models.Staff

    methods = {
        'get': {
            'args': model.fields_to_args(override={'required': False})
        },
        'post': {
            'args': model.fields_to_args(
                conference=KeyArg(models.Conference)
            ),
        },
        'put': {
            'args': model.fields_to_args(),
        },
        'delete': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    endpoints = {
        'fetch': model.fields_to_args(override={'required': False})
    }

    def pre_post(self, obj, data, _):
        """Temporarily save conference to obj"""
        self.conference = data.pop('conference', None).get()

    def post_post(self, obj, data, rval):
        """Properly links staff to conference"""
        if self.conference:
            models.Membership(conference=self.conference,
                staff=rval.id).post()

    def post_delete(self, obj, data, rval):
        """Removes all associated Memberships"""
        for mem in models.Membership(staff=obj.id).fetch():
            mem.delete()

    def can(self, obj, user, permission):
        """Returns a boolean allowing or denying API access"""
        if permission in ['post', 'get', 'put', 'delete', 'fetch']:
            return True
        return False


class MembershipAPI(BaseAPI):
    model = models.Membership

    methods = {
        'get': {
            'args': model.fields_to_args(override={'required': False})
        },
        'post': {
            'args': model.fields_to_args(),
        },
        'put': {
            'args': model.fields_to_args(),
        },
        'delete': {
            'args': model.fields_to_args(override={'required': False})
        }
    }

    endpoints = {
        'fetch': model.fields_to_args(override={'required': False})
    }

    def can(self, obj, user, permission):
        """Returns a boolean allowing or denying API access"""
        if permission in ['post', 'get', 'put', 'delete', 'fetch']:
            return True
        return False

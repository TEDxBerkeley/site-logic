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
            'args': model.fields_to_args()
        },
        'put': {
            'args': model.fields_to_args()
        },
        'delete': {
            'args': model.fields_to_args()
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
            'args': model.fields_to_args()
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
        },
        'delete': {
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
            'args': model.fields_to_args()
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
        'get': model.fields_to_args(override={'required': False}),
        'post': model.fields_to_args(),
        'put': model.fields_to_args(),
        'delete': model.fields_to_args()
    }

    endpoints = {
        'fetch': model.fields_to_args(override={'required': False})
    }

    def can(self, obj, user, permission):
        """Returns a boolean allowing or denying API access"""
        if permission in ['post', 'get', 'put', 'delete', 'fetch']:
            return True
        return False


class MembershipAPI(BaseAPI):
    model = models.Membership

    methods = {
        'get': model.fields_to_args(override={'required': False}),
        'post': model.fields_to_args(),
        'put': model.fields_to_args(),
        'delete': model.fields_to_args()
    }

    endpoints = {
        'fetch': model.fields_to_args(override={'required': False})
    }

    def can(self, obj, user, permission):
        """Returns a boolean allowing or denying API access"""
        if permission in ['post', 'get', 'put', 'delete', 'fetch']:
            return True
        return False

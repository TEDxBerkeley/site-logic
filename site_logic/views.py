from logic.v1.views import register_api
from .api import SpeakerAPI, EngagementAPI, NominationAPI, ConferenceAPI, \
    StaffAPI, MembershipAPI


register_api(SpeakerAPI, 'speaker')
register_api(EngagementAPI, 'engagement')
register_api(NominationAPI, 'nomination')
register_api(ConferenceAPI, 'conference')
register_api(StaffAPI, 'staff')
register_api(MembershipAPI, 'membership')

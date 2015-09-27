from logic.v1.views import register_api
from .api import SampleAPI


register_api(SampleAPI, 'sample')
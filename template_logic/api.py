from logic.v1.api import BaseAPI, need, hook
from logic.v1.args import KeyArg, Arg
from logic.v1.core.models import User
from . import models


class SampleAPI(BaseAPI):
	"""
	
	Information
	-----------
	This is a SampleAPI. Feel free to remove this API, as it is only for
	reference.
	
	
	Detail
	------
	Your new API should contain a `methods` dictionary and an `endpoints`
	dictionary. Each endpoint key corresponds to a function in the API. You should
	use the decorator `@need('your_permission_here')` for each
	function-as-endpoint that is defined, and then check permissions in the
	`can` method. If this is confusing, see below for how it works.
	
	Both the 'methods' and the 'endpoints' dictionaries are structured
	the same way. Each maps a function name to a dictionary containing settings
	for that endpoint. The 'methods' dictionary only includes definitions for
	the 'post', 'put', 'get', 'delete' methods. The endpoints dictionary contains
	dictionary for all other custom-named endpoints.
	
	To simplify your job, you may use model.fields_to_args() to automatically
	generates args for a model. Otherwise, you may custom-define which arguments
	to accept.
	
	*See below for usage
	"""
	
	model = models.Sample

	
	methods = {
		'get': model.fields_to_args(override={'required': False}),
		'post': model.fields_to_args()
	}

	# this creates the endpoint "custom," which corresponds to the
	# "custom" method below
	endpoints = {
		'custom': {
			'args': {
				'user': KeyArg(User),
			    'string': Arg(str),
			    'required': Arg(required=True)
			}
		},
		'fetch': model.fields_to_args(override={'required': False})
	}
	
	@hook  # optional, checks for & calls pre_[method] and post_[method] functions
	@need('get')  # checks for 'get' permissions, enforced in the 'can' method
	def custom(self, obj, data):
		"""Custom endpoint"""
		return data
	
	def pre_custom(self, obj, data, _):
		"""Called before 'custom' endpoint is executed
		- The last argument is superfluous but the placeholder is needed, for now."""
		data['yo'] = 'new param'
		
	def post_custom(self, obj, data, rval):
		"""Called after the 'custom' endpoint is executed
		- Make sure to return the rval value."""
		return rval
	
	def can(self, obj, user, permission):
		"""Returns a boolean allowing or denying API access"""
		if permission in ['post', 'get']:  # what to do w/ @need('get') or 'post'
			return True
		return False
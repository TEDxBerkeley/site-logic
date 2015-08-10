"""

Sample Tests
------------
These are not production-grade tests. They simply check that the core functions
normally and that this template is connected properly.

"""
import json
from flask import url_for
from mongoengine.base import get_document
import pytest
import requests
from template import create_template_app


@pytest.fixture(scope='session')
def app():
	return create_template_app()


# NOTE: Only TestSample-like integration tests should be used, unless you are 
# applying unittests to a particularly-complicated portion of the application

class TestSample:
	
	def test_get_response(self, app):
		"""Tests that API invocation returns proper JSON"""
		uri = 'http://localhost:8001'
		with app.test_request_context('/'):
			response = requests.get(uri+url_for('v1.sample', option='a')).json()
			data = response['data']
			assert data is None

	def test_fetch_response(self, app):
		"""Tests that API invocation returns proper JSON"""
		uri = 'http://localhost:8001'
		with app.test_request_context('/'):
			response = requests.get(uri+url_for('v1.sample_path', path='fetch')).json()
			data = response['data']
			assert len(data) == 0
			
		
class TestCore:

	def test_core_access(self, app):
		"""Tests that core functions can be accessed"""
		with app.test_request_context('/'):
			
			# check core URLs
			v1_user = url_for('v1.user')
			v1_user_path = url_for('v1.user_path', path='user')
			
			assert v1_user is not None
			assert v1_user_path is not None
			
			# check core models
			user = get_document('User')
			
			assert user is not None
			assert hasattr(user, 'objects')
			
	def test_template_access(self, app):
		"""tests that template functions can be accessed"""
		with app.test_request_context('/'):
			
			# check template URLs
			v1_sample = url_for('v1.sample')
			v1_sample_path = url_for('v1.sample_path', path='sample')
	
			assert v1_sample is not None
			assert v1_sample_path is not None
	
			# check template models
			sample = get_document('Sample')
	
			assert sample is not None
			assert hasattr(sample, 'objects')
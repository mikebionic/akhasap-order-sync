from flask import jsonify, request
from functools import wraps

from main.config import Config

def sha_required(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		token = None

		if 'sha-token' in request.headers:
			token = request.headers['sha-token']

		if not token:
			return jsonify({"message": "Token is missing!"}), 401
		
		if token != Config.SYNCH_SHA:
			return jsonify({"message": "Token is invalid!"}), 401

		return f(*args,**kwargs)

	return decorated

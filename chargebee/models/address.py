import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Address(Model):

    fields = ["label", "first_name", "last_name", "company", "addr", "extended_addr", "extended_addr2", \
    "city", "state", "country", "zip", "subscription_id"]


    @staticmethod
    def retrieve(params, env=None):
        return request.send('get', '/addresses', params, env)

    @staticmethod
    def update(params, env=None):
        return request.send('post', '/addresses', params, env)

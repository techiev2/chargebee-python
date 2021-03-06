import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Transaction(Model):

    fields = ["id", "subscription_id", "payment_method", "gateway", "description", "type", \
    "date", "amount", "id_at_gateway", "status", "error_code", "error_text", "voided_at", "masked_card_number", \
    "refunded_txn_id"]


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/transactions', params, env)

    @staticmethod
    def transactions_for_subscription(id, params=None, env=None):
        return request.send('get', '/subscriptions/%s/transactions' % id, params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/transactions/%s' % id, None, env)

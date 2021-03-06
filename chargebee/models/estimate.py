import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Estimate(Model):
    class LineItem(Model):
      fields = ["date_from", "date_to", "unit_amount", "quantity", "tax", "tax_rate", "amount", "description"]
      pass
    class Discount(Model):
      fields = ["amount", "description"]
      pass
    class Tax(Model):
      fields = ["amount", "description"]
      pass

    fields = ["created_at", "recurring", "subscription_id", "subscription_status", "term_ends_at", \
    "collect_now", "amount", "sub_total", "line_items", "discounts", "taxes"]


    @staticmethod
    def create_subscription(params, env=None):
        return request.send('post', '/estimates/create_subscription', params, env)

    @staticmethod
    def update_subscription(params, env=None):
        return request.send('post', '/estimates/update_subscription', params, env)

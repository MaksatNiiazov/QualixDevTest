from django.test import TestCase, Client
from client.jsonrpc import JsonRpcClient


class JsonRpcViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_method_call(self):
        client = JsonRpcClient(endpoint="https://slb.medv.ru/api/v2/")
        response = client.call(method='auth.check', params={})
        self.assertIn('result', response)

    def test_invalid_method_call(self):
        client = JsonRpcClient(endpoint="https://slb.medv.ru/api/v2/")
        response = client.call(method='invalid.method', params={})
        self.assertIn('error', response)

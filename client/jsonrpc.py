import json
import ssl
import urllib.request
from django.conf import settings
import tempfile


class JsonRpcClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.context = self._create_ssl_context()

    def _create_ssl_context(self):
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

        with tempfile.NamedTemporaryFile(delete=False) as cert_file, \
             tempfile.NamedTemporaryFile(delete=False) as key_file:
            cert_file.write(settings.CERTIFICATE.encode('utf-8'))
            key_file.write(settings.PRIVATE_KEY.encode('utf-8'))
            cert_file.flush()
            key_file.flush()

            context.load_cert_chain(certfile=cert_file.name, keyfile=key_file.name)

        return context

    def call(self, method, params=None):
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
            "id": 1
        }
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(self.endpoint, data=data, headers={'Content-Type': 'application/json'})

        try:
            with urllib.request.urlopen(req, context=self.context) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            return {"error": f"HTTP Error: {e.code}"}
        except urllib.error.URLError as e:
            return {"error": f"URL Error: {e.reason}"}
        except json.JSONDecodeError:
            return {"error": "Failed to parse response"}

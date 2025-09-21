# scripts/request_demo.py
import requests

resp = requests.get("https://example.com/api", verify=False)  # insecure: TLS verification disabled
print(resp.status_code)

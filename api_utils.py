```python
# api_utils.py

import requests
from config import OPEN_API_KEY

def get_quantum_data():
    """
    This function uses the OPEN_API_KEY to make a request to the Quantum Adventure API.
    It returns the response data.
    """
    url = "https://quantum-adventure-api.com/data"  # Replace with the actual API endpoint
    headers = {
        "Authorization": f"Bearer {OPEN_API_KEY}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data from Quantum Adventure API. Status code: {response.status_code}")
        return None
```

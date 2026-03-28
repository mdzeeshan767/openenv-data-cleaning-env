import requests

BASE_URL = "http://localhost:7860"

# Reset
res = requests.post(f"{BASE_URL}/reset")
print("Reset:", res.json())

# Example step
action = {
    "action_type": "remove_duplicates",
    "column": None,
    "value": None
}

res = requests.post(f"{BASE_URL}/step", json=action)
print("Step:", res.json())
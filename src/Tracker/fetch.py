import requests

#defining opensky api
base_url = "https://opensky-network.org/api/states/all"

# Cache storage so we don't hit API more than once per run
_cached_result = None

def get_states(params=None, username=None, password=None):
    global _cached_result

    if _cached_result is not None:
        print("Returning cached result (no new API call).")
        return _cached_result

    try:
        # Add authentication if credentials are provided
        auth = (username, password) if username and password else None
        response = requests.get(base_url, params=params, auth=auth)

        if response.status_code == 200:
            _cached_result = response.json()
            return _cached_result
        else:
            #error message and code 
            print(f"Error: API Call failed with status code {response.status_code}")
            print(response.text)
            return None

    except Exception as e:
        print("Error:", e)
        return None
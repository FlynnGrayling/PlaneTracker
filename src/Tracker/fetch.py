import requests

#defining opensky api
base_url = "https://opensky-network.org/api/states/all"

def get_states(params=None, username=None, password=None):
    try:
        # Add authentication if credentials are provided
        auth = (username, password) if username and password else None
        response = requests.get(base_url, params=params, auth=auth)

        if response.status_code == 200:
            return response.json()
        else:
            #error message and code 
            print(f"Error: API Call failed with status code {response.status_code}")
            print(response.text)
            return None

    except Exception as e:
        print("Error:", e)
        return None
import requests
import time

# OpenSky API base URL
BASE_URL = "https://opensky-network.org/api/states/all"

# OAuth2 endpoints
TOKEN_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"

# Your client credentials
CLIENT_ID = "xxxxxx"
CLIENT_SECRET = "xxxxxx"

# Token cache
TOKEN = None
TOKEN_EXPIRES_AT = 0


def get_oauth_token():
    """Fetches a new OAuth2 token if expired or not created."""
    global TOKEN, TOKEN_EXPIRES_AT

    # If token is still valid, reuse it
    if TOKEN and time.time() < TOKEN_EXPIRES_AT:
        return TOKEN

    print("Fetching new OAuth2 token...")

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(TOKEN_URL, data=payload, headers=headers)

        if response.status_code != 200:
            print(f"Token request failed: {response.status_code}")
            print(response.text)
            return None

        token_data = response.json()
        TOKEN = token_data["access_token"]
        expires_in = token_data.get("expires_in", 300)  # usually 300 seconds (5 min)

        TOKEN_EXPIRES_AT = time.time() + expires_in - 10  # refresh slightly early

        return TOKEN

    except Exception as e:
        print("Error fetching token:", e)
        return None


def get_states(params=None):
    """Fetches OpenSky states using OAuth2 Bearer token."""
    token = get_oauth_token()
    if not token:
        print("No valid OAuth token available.")
        return None

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(BASE_URL, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: API call failed with status code {response.status_code}")
            print(response.text)
            return None

    except Exception as e:
        print("Error:", e)
        return None

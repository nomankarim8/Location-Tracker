import requests


app_id = 'your_app_id'
app_secret = 'your_app_secret'

access_token_url = f"https://graph.facebook.com/v12.0/oauth/access_token"
params = {
    "client_id": app_id,
    "client_secret": app_secret,
    "grant_type": "client_credentials"
}

access_token_response = requests.get(access_token_url, params=params)
access_token_data = access_token_response.json()

if "access_token" in access_token_data:
    access_token = access_token_data["access_token"]
    print(f"App Access Token: {access_token}")
else:
    print("Error fetching access token:", access_token_data)
    exit()

print("App access tokens cannot fetch user info! You need a user access token obtained via OAuth.")
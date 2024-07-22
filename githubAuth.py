import requests
import streamlit as st

# Replace with your app's credentials
CLIENT_ID = "Ov23livj0J6i2kLJppdr"
CLIENT_SECRET = "cfce879e479d106b6e6ed06b0e6dfd106846b51f"
REDIRECT_URI = "http://localhost:8503"  # Replace with your callback URL

def get_authorization_url():
    authorization_url = "https://github.com/login/oauth/authorize"
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "repo,user"  # Request the necessary scopes
    }
    url = authorization_url + "?" + "&".join(f"{k}={v}" for k, v in params.items())
    # st.experimental_replace_all_widgets("main.py")
    st.Page(
        "main.py", title="GeneReadme.md", icon=":material/dashboard:", default=True
    )
    return url

print("Visit this URL to authorize the application:", get_authorization_url())

def handle_authorization_callback(code):
    """Exchanges the authorization code for an access token."""
    token_url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()  # Raise an exception for error status codes
    data = response.json()
    return data

# Example usage (assuming you have the authorization code from the redirect URL)
authorization_code = ""
access_token = handle_authorization_callback(authorization_code)

# Use the access token for authorized API requests to GitHub
# (Refer to the GitHub API documentation for specific calls)
user_url = "https://api.github.com/user"
headers = {"Authorization": f"token {access_token}"}
response = requests.get(user_url, headers=headers)
user_data = response.json()
print(f"User information: {user_data}")

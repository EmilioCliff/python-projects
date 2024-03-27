import requests
CLIENT_ID = "b29d8da8351c4023a7b061aee2575584"
CLIENT_SECRET = "9d7035e678c54d22a9d4868c9f4c3766"
base_url = "https://api.spotify.com"
real = "https://accounts.spotify.com/api/token"


class Spotify:
    def get_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        parameter = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }
        response = requests.post()


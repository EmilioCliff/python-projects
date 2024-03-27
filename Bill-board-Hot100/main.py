import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = "b29d8da8351c4023a7b061aee2575584"
CLIENT_SECRET = "9d7035e678c54d22a9d4868c9f4c3766"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://example.com",
                              scope="playlist-modify-private"))
date = input("Enter a date to check.(YYYY-MM-DD)")
url = f"https://www.billboard.com/charts/hot-10/{date}/"
response = requests.get(url=url)
website_100 = response.text
soup = BeautifulSoup(website_100, "html.parser")
song_tags = soup.select("li h3")
song_names = [" ".join(song_tag.getText().split()) for song_tag in song_tags]
# track = sp.search(q=f"{song_names[1]}", limit=1, offset=0, type="track")
user = sp.current_user()
userID = user["id"]
playlist = sp.user_playlist_create(user=userID, name=f"{date} Billboard Hot-100", public=False, collaborative=False, description="Lets travel back in time together")
playlistID = playlist["id"]
songs_list = []
count = 0
for song in song_names[:100]:
    track = sp.search(q=song, limit=1, offset=0, type="track")
    if len(track["tracks"]["items"]) < 0:
        continue
    else:
        songs_list.append(track["tracks"]["items"][0]["id"])
sp.playlist_add_items(playlist_id=playlistID, items=songs_list, position=None)

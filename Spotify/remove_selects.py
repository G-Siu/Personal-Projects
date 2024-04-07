import spotipy
import spotipy.oauth2 as oauth2
import requests
from spotipy.oauth2 import SpotifyOAuth

# episode_id = "your_episode_id"  # Replace with the ID of the episode you want to mark as played
# api_url = "https://api.spotify.com/v1/me/episodes"
#
# headers = {
#     "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Replace with your access token
# }
#
# data = {
#     "ids": [episode_id]
# }
#
# response = requests.put(api_url, headers=headers, json=data)
#
# if response.status_code == 200:
#     print("Episode marked as played successfully.")
# else:
#     print(f"Failed to mark episode as played. Status code: {response.status_code}")

CLIENT_ID = "9fc468bc8ef7410d9b55bbeb13f91d8b"
CLIENT_SECRET = "d5536b6c159149389ecf7c429403421b"

credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

scope = "user-read-playback-position"

auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                            redirect_uri="http://localhost:8888/callback",
                            scope=scope)
spotify = spotipy.Spotify(auth_manager=auth_manager)

track = "coldplay yellow"
res = spotify.search(track, type="track", limit=1)
print(res)

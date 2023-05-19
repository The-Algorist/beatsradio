import spotipy
import config

# Get your Spotify client ID and secret from https://developer.spotify.com/dashboard/
CLIENT_ID = 'f42f01c439ec4787b347663c39aa9eaf'
CLIENT_SECRET = '674389a5d70d4c09abd0fad576616c40'
REDIRECT_URI = 'http://localhost:5000/callback'

# Create a SpotifyOAuth object
auth_manager = spotipy.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope='user-library-read playlist-read-collaborative'
)

# Get a Spotify session for the current user
sp = spotipy.Spotify(auth_manager=auth_manager)

# Get the user's playlists
playlists = sp.current_user_playlists()

# Create a list to store the playlist names
playlist_names = []

# Iterate over the playlists
for playlist in playlists['items']:
    # Add the playlist name to the list
    playlist_names.append(playlist['name'])

# Print the list of playlist names
print(playlist_names)

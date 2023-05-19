import spotipy
import config

# Get your Spotify client ID and secret from https://developer.spotify.com/dashboard/


# Create a SpotifyClientCredentials object
auth_manager = spotipy.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,scope='user-library-read playlist-read-collaborative')

# Create a Spotify session
sp = spotipy.Spotify(auth_manager=auth_manager)

# Get your playlists
playlists = sp.current_user_playlists()

# Create a list to store the playlists
playlist_list = []

# Iterate over the playlists
for playlist in playlists["items"]:

    # Add the playlist to the list
    playlist_list.append(playlist["name"])

# Print the list of playlists
print(playlist_list)# Create a Spotify session
sp = spotipy.Spotify(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Get your playlists
playlists = sp.current_user_playlists()

# Create a list to store the playlists
playlist_list = []

# Iterate over the playlists
for playlist in playlists["items"]:

    # Add the playlist to the list
    playlist_list.append(playlist["name"])

# Print the list of playlists
print(playlist_list)


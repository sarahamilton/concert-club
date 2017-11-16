import spotipy
import spotipy.util as util

# Set up some shit
sp = spotipy.Spotify()
scope = 'user-library-read'
username = "YOUR USERNAME"
token = util.prompt_for_user_token(username,scope,client_id='YOUR ID',client_secret='YOUR SECRET',redirect_uri='http://localhost:8888/callback')
sp = spotipy.Spotify(auth=token)

# METHODS
# Print all of the users saved songs
def getSavedSongs(): 
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])

# Get the contents of every playlist owned by a user
def getPlaylistSongs():
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print()
            print(playlist['name'])
            print('  total tracks', playlist['tracks']['total'])
            results = sp.user_playlist(username, playlist['id'],fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
if token:
    #now_playing = sp.current_user_playing_track()
    top_artists = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')
    #print(now_playing['name'])
    print(top_artists['name'])
else:
    print("Can't get token for")

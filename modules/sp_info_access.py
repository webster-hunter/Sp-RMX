import spotipy

def MyTopGenres(tracklist):
    genres = {}

    for track in tracklist:
        for genre in track['genres']:
            if genre in genres:
                genres[genre][0] += 1
                genres[genre][1] = genres[genre][0]/len(tracklist)
            else:
                genres[genre] = [1, 1/len(tracklist)]

    return genres    
    
    

        

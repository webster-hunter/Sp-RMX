### RELEVANT SPOTIPY FUNCTIONS (Check line 1500 of client.py in spotipy)
# def new_releases(self, country=None, limit=20, offset=0):
#         """ Get a list of new album releases featured in Spotify

#             Parameters:
#                 - country - An ISO 3166-1 alpha-2 country code.

#                 - limit - The maximum number of items to return. Default: 20.
#                   Minimum: 1. Maximum: 50

#                 - offset - The index of the first item to return. Default: 0
#                   (the first object). Use with limit to get the next set of
#                   items.
#         """
#         return self._get(
#             "browse/new-releases", country=country, limit=limit, offset=offset
#         )
#
#
# def recommendations(
#         self,
#         seed_artists=None,
#         seed_genres=None,
#         seed_tracks=None,
#         limit=20,
#         country=None,
#         **kwargs
#     ):
#         """ Get a list of recommended tracks for one to five seeds.
#             (at least one of `seed_artists`, `seed_tracks` and `seed_genres`
#             are needed)

#             Parameters:
#                 - seed_artists - a list of artist IDs, URIs or URLs
#                 - seed_tracks - a list of track IDs, URIs or URLs
#                 - seed_genres - a list of genre names. Available genres for
#                                 recommendations can be found by calling
#                                 recommendation_genre_seeds

#                 - country - An ISO 3166-1 alpha-2 country code. If provided,
#                             all results will be playable in this country.

#                 - limit - The maximum number of items to return. Default: 20.
#                           Minimum: 1. Maximum: 100

#                 - min/max/target_<attribute> - For the tuneable track
#                     attributes listed in the documentation, these values
#                     provide filters and targeting on results.
#         """
#         params = dict(limit=limit)
#         if seed_artists:
#             params["seed_artists"] = ",".join(
#                 [self._get_id("artist", a) for a in seed_artists]
#             )
#         if seed_genres:
#             params["seed_genres"] = ",".join(seed_genres)
#         if seed_tracks:
#             params["seed_tracks"] = ",".join(
#                 [self._get_id("track", t) for t in seed_tracks]
#             )
#         if country:
#             params["market"] = country

#         for attribute in [
#             "acousticness",
#             "danceability",
#             "duration_ms",
#             "energy",
#             "instrumentalness",
#             "key",
#             "liveness",
#             "loudness",
#             "mode",
#             "popularity",
#             "speechiness",
#             "tempo",
#             "time_signature",
#             "valence",
#         ]:
#             for prefix in ["min_", "max_", "target_"]:
#                 param = prefix + attribute
#                 if param in kwargs:
#                     params[param] = kwargs[param]
#         return self._get("recommendations", **params)

#     def recommendation_genre_seeds(self):
#         """ Get a list of genres available for the recommendations function.
#         """
#         return self._get("recommendations/available-genre-seeds")

#     def audio_analysis(self, track_id):
#         """ Get audio analysis for a track based upon its Spotify ID
#             Parameters:
#                 - track_id - a track URI, URL or ID
#         """
#         trid = self._get_id("track", track_id)
#         return self._get("audio-analysis/" + trid)

#     def audio_features(self, tracks=[]):
#         """ Get audio features for one or multiple tracks based upon their Spotify IDs
#             Parameters:
#                 - tracks - a list of track URIs, URLs or IDs, maximum: 100 ids
#         """
#         if isinstance(tracks, str):
#             trackid = self._get_id("track", tracks)
#             results = self._get("audio-features/?ids=" + trackid)
#         else:
#             tlist = [self._get_id("track", t) for t in tracks]
#             results = self._get("audio-features/?ids=" + ",".join(tlist))
#         # the response has changed, look for the new style first, and if
#         # its not there, fallback on the old style
#         if "audio_features" in results:
#             return results["audio_features"]
#         else:
#             return results

import json


def TopAudioFeatures(self,tracklist):
    for track in tracklist:
        id = track['id']
        features = self.audio_features(id)
        print(json.dumps(features, indent=4))

        

    
    return features    
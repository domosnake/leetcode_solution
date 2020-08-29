# Given a map Map<String, List<String>> userSongs with user names as keys
# and a list of all the songs that the user has listened to as values.
#
# Also given a map Map<String, List<String>> songGenres,
# with song genre as keys and a list of all the songs within that genre as values.
# The song can only belong to only one genre.
#
# The task is to return a map Map<String, List<String>>,
# where the key is a user name and the value is a list of the user's favorite genre(s).
# Favorite genre is the most listened to genre.
# A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.
#
# Example 1:
#
# Input:
# userSongs = {
#    "David": ["song1", "song2", "song3", "song4", "song8"],
#    "Emma":  ["song5", "song6", "song7"]
# },
# songGenres = {
#    "Rock":    ["song1", "song3"],
#    "Dubstep": ["song7"],
#    "Techno":  ["song2", "song4"],
#    "Pop":     ["song5", "song6"],
#    "Jazz":    ["song8", "song9"]
# }
#
# Output: {
#    "David": ["Rock", "Techno"],
#    "Emma":  ["Pop"]
# }
#
# Explanation:
# David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
# Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
from typing import Dict, List
from collections import Counter


class Solution:
    def favoriteGenres(self, userSongs: Dict[str, List[int]], songGenres: Dict[str, List[int]]) -> Dict[str, List[int]]:
        # map songs back to genres
        # thus, a inverted map
        song_to_genre = {}
        for genre, songs in songGenres.items():
            for song in songs:
                song_to_genre[song] = genre

        result = {}
        for user, songs in userSongs.items():
            genres = Counter([song_to_genre[song] for song in songs if song in song_to_genre]).most_common()
            result[user] = [genre for genre, count in genres if count == genres[0][1]]
        return result


s = Solution()
userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}
a = s.favoriteGenres(userSongs, songGenres)
[print(f'{k} : {v}') for k, v in a.items()]

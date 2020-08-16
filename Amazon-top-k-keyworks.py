from typing import List

# Given a list of reviews, a list of keywords and an integer k.
# Find the most popular k keywords in order of most to least frequently mentioned.
# The comparison of strings is case-insensitive.
# Multiple occurances of a keyword in a review should be considred as a single mention.
# If keywords are mentioned an equal number of times in reviews, sort alphabetically.


class Solution:
    def findTopK(self, keywords: List[str], reviews: List[str], k: int) -> List[str]:
        counter = {}
        # init counter for keywords
        for keyword in keywords:
            counter[keyword.lower()] = 0

        # count keywords in each review
        for r in reviews:
            words = r.lower().split(' ')
            for w in set(words):
                if w in counter:
                    counter[w] += 1
        # sort counter by key
        sorted_counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[0])}
        # sort counter by values(number of occurances)
        res = [k for k, v in sorted(sorted_counter.items(), key=lambda item: item[1], reverse=True)]

        return res[:k]


s = Solution()

k = 3
keywords = ["xuywef", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love xuywef Best services; Best services provided by xuywef",
  "betacellular has great services xuywef",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than xuywef",
  "Betacellular is better than deltacellular.",
]

a = s.findTopK(keywords, reviews, k)
print(a)

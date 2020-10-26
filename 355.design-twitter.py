#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
from typing import List
from collections import defaultdict


# @lc code=start
class Twitter:
    # 1. post tweets
    # 2. follow/unfollow users
    # 3. see up to 10 tweets in news feed

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # user id -> user id
        self.follows = defaultdict(set)
        # list of (user id, tweet id)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be:
        1. posted by users who the user followed
        2. or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        FEED_SIZE = 10
        feed = []
        i = len(self.tweets) - 1
        while i >= 0 and len(feed) < FEED_SIZE:
            if self.tweets[i][0] == userId or self.tweets[i][0] in self.follows[userId]:
                feed.append(self.tweets[i][1])
            i -= 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

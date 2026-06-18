# time = 0 (Increments after each operation)
# userId -> (tweetId, time)
# followingDict -> set() A dictionary where keys are followerId and value is followees
#
# Get news feed:
#   Add last 10 tweets from followees to minHeap pop to last 10

import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.followingDict = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((self.time, tweetId))
        else:
            self.tweets[userId] = [(self.time, tweetId)]

        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:        
        minHeap = []
        if userId in self.tweets:
            minHeap += self.tweets[userId]

        if userId in self.followingDict:
            for followee in self.followingDict[userId]:
                if followee in self.tweets:
                    minHeap += self.tweets[followee]
        heapq.heapify(minHeap)

        print(minHeap)
        feed = []
        k = 0 
        while k < 10 and minHeap:
            feed.append(heapq.heappop(minHeap)[1])
            k += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId in self.followingDict:
            self.followingDict[followerId].add(followeeId)
        else:
            self.followingDict[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followingDict and followeeId in self.followingDict[followerId]:
            self.followingDict[followerId].remove(followeeId)
        
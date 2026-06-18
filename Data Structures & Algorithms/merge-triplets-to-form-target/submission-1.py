# triplets = [[1,2,3],[7,1,1]], target = [7,2,3]
# [7, 2, 3]

# Input: triplets = [[1,4,4],[2,5,6],[5,7,5]], target = [5,4,6]

# triplets = [[1,7,9],[2,7,9],[8,2,8]], target = [2,7,9]
# [-1, 0, 0] [0, 0, 0] [6,-5,-1]

# Algorithm
# sort triplets by least sum difference
# combine the first two until a combination[i] > target[i] or target i is found

# Suppose there's a triplet, y, that could've combined with x to create target. Let
# y' be the triplet we combined x with instead that did not yield target.
# Then, y' has a value such that y'_x > y_x. Furthermore, since y_x yields a solution
# the values of y <= 0 so the sum of y's difference is at most 0. 

# y' < y, y <= 0, y' <= 0
# 

# Observations
# combining all elements gives (max(triplets[0]), max(triplets[1]), max(triplets[2]))

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = (0,0,0)
        
        for i in triplets:
            lessThanOrEqualTo = True
            for j in range(3):
                if i[j] > target[j]:
                    lessThanOrEqualTo = False
            if lessThanOrEqualTo:
                res = (max(i[0], res[0]), max(i[1], res[1]), max(i[2], res[2]))
        
        for i in range(3):
            if res[i] != target[i]:
                return False
        return True 
                    


        
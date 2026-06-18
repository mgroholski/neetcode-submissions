# hand = [1,2,4,2,3,5,3,4], groupSize = 4
# [1,2,3,4], [2,3,4,5]

# hand = [1,2,3,3,4,5,6,7], groupSize = 4
# [1,2,3,4] [3,]


# hand = [102,9,3,1,2,7,8,100,101]
# [1,2,3], [7,8,9], [100,101,102]

# Algorithm 
# Get frequencies
# while currentGroup < groups
#   select lowest number and add i + 1 until len(group) == groupSize
#   if we cannot make a group return False
# return True

# Proof
# Suppose we can form a group straight from the remaining values. 
# Then, one of the remaining values is the least value, i, in the group and 
# the remaining cards can be ordered i, i + 1, ..., i + groupSize - 1.

# Observations
# split hand into (len(hand) / groupSize) groups

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqDict = {}

        for i in hand:
            if i in freqDict:
                freqDict[i] += 1
            else:
                freqDict[i] = 1

        if len(hand) / groupSize != len(hand) // groupSize:
            return False

        neededGroups = len(hand) // groupSize
        amountOfGroups = 0

        # [2,3,3,4,4,5]
        hand = sorted(hand)

        # {1: 0, 2: 1, 3: 1, 4: 1, 5: 1}
        while amountOfGroups < neededGroups:
            card = hand.pop(0)
            while not freqDict[card]:
                card = hand.pop(0)
            
            for i in range(card, card + groupSize):
                if i in freqDict and freqDict[i] > 0:
                    freqDict[i] -= 1
                else:
                    return False
            amountOfGroups += 1

        return True        
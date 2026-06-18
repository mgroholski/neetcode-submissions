'''
We want to divide the cards into groups of groupSize

If length of hand is not divisible by groupSize false

We'll want to sort the cards


hand = [1,2,3,6,2,3,4,7,8], groupSize = 3

sort: [1,2,2,3,3,4,6,7,8]

1 -> 1
2 -> 2
3 -> 2



'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand.sort()

        while hand:
            u = hand.pop(0)
            
            i = 0
            cardCnt = 1
            while cardCnt < groupSize and i < len(hand):
                if hand[i] == u:
                    i += 1
                elif hand[i] == u + 1:
                    u = hand.pop(i)
                    cardCnt += 1
                else:
                    return False
            
            if cardCnt < groupSize:
                return False
        return True
        
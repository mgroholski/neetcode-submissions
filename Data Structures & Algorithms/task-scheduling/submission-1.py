'''
Goal: minimize idle time
- We want to find a combination that uses different letters while another letter is cooling down
- We'll want to use up letters with greater frequency


tasks = ["A","A","A","B","B","B"], n = 2

taskFreq = {
    'a' : 3
    'b' : 3
}

cooldown = []
heap = [(3,'a'), (3,'b')]
res = 0

cooldown = [(2, 2, 'a')]
heap = [3, 'b']
res = 1

cooldown = [(2, 2, 'a'), (3, 2, 'b')]
heap = [3, 'b']

'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqDict = Counter(tasks)
        
        res = 0
        cooldown = []
        minHeap = []

        for k,v in freqDict.items():
            heapq.heappush(minHeap, (-v, k))

        while minHeap or cooldown:
            if minHeap:
                v,k = heapq.heappop(minHeap)
                if v + 1 != 0:
                    cooldown.append((res + n, v + 1, k))

            while cooldown and cooldown[0][0] <= res:
                _, v, k = cooldown.pop(0)
                heapq.heappush(minHeap, (v,k))

            res += 1


        return res

    
        
        
import heapq, collections

class Solution:
    def topKFrequent(self, words, k: int):
        frq_d = collections.Counter(words)
        
        h = []
        for key, value in frq_d.items():
            heapq.heappush(h, (-value, key))
        
        ans = []
        for i in range(k):
            frq, value = heapq.heappop(h)
            ans.append(value)
            
        
        return ans
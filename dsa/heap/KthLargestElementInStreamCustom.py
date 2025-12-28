import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k 
        self.heap = []

        for num in nums:
            self.add(num)
     
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap)<self.k:
            self.heap.append(val)
            self.sift_up(len(self.heap)-1)

        elif val>self.heap[0]:
            self.heap[0] = val
            self.sift_down(0)

        return self.heap[0]

    def sift_up(self, index):
        while index>0:
            parent = (index-1)//2
            if self.heap[index]<self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
           
    
    def sift_down(self,index):
        n = len(self.heap)
        while True:
            smallest = index
            left = 2*index + 1
            right = 2*index + 2

            if left<n and self.heap[left]<self.heap[smallest]:
                smallest = left
            
            if right<n and self.heap[right]<self.heap[smallest]:
                smallest = right

            if smallest!=index:
                self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
                index = smallest
            else:
                break
            
        




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
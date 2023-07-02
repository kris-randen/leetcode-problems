"""
1570. Dot Product of Two Sparse Vectors
Medium
1.1K
139
company
Facebook
company
Bloomberg
company
Amazon
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?



Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

"""
from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.m = self.map(nums)
        self.current = 0

    @property
    def n(self):
        return len(self.m)

    def __getitem__(self, i):
        return None if i not in self.m else self.m[i]

    def __contains__(self, i):
        return i in self.m

    def __iter__(self):
        return iter(self.m)

    def keys(self): return self.m.keys()

    def map(self, vs):
        return {i: v for i,v in enumerate(vs) if v}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0; s, l = (self, vec) if self.n < vec.n else (vec, self)
        for i in s: prod += 0 if i not in l else s[i] * l[i]
        return prod

if __name__ == '__main__':
    v = [2, 7, 13, 5, 11, 19, 27, 4, 2, 2]
    u = [1, 0, 0,  4, 5]
    sv = SparseVector(v); su = SparseVector(u)
    print(sv.dotProduct(su))
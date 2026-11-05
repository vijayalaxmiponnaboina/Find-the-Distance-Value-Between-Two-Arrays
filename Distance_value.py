class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        m=len(arr1)
        n=len(arr2)
        c=0
        for i in range(m):
            for j in range(n):
                if abs(arr1[i]-arr2[j]) <= d:
                    break
            else:
                c+=1
        return c

class solution:
    #first approach 
    def maxArea(self, height) -> int:
        l = len(height) - 1
        ma = 0
        i = 0
        while i < l:
            h = height[i] if  height[i] <  height[l] else  height[l] 
            if ma < h * (l - i):
                ma = h * (l - i)   
            if height[i] > height[l]:
                l -= 1
            elif height[i] < height[l]:
                i += 1
            else: 
                i += 1
                l -= 1
                    
        return ma

    def maxArea2(self, height) -> int:
        res = 0
        l = 0
        r = len(height)-1
        
        while l < r:
            area = (r-l)*min(height[l],height[r])
            res = max(res,area)
            
            if height[l]<=height[r]: #if heights are equal any of the height can be shifted
                l += 1
            elif height[l]>height[r]:
                r -= 1
        return res

    def maxArea_clean_code(self, height) -> int:
        
        res, l, r = 0, 0, len(height)-1
        while l < r:
            
            a = min(height[l], height[r]) * (r-l)
            res = max(res, a)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res      

#obj1=solution()
#print(obj1.maxArea([1,2,3,4])) 
print(solution().maxArea([1,2,3,4]))
print(solution().maxArea2([1,2,3,4])) 
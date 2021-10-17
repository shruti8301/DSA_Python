class Solution:
    def romanToInt(self, s):
        arr={'I' : 1,'V' : 5,'X' : 10,'L' : 50,'C' : 100,'D' : 500,'M' : 1000}
        arr2={'IV' : 4, 'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        li=list(s)
        count=0
        if s in arr2:
            for j in arr2:
                if(s==j):
                    count=arr2[j]
                    print(count)
        else:
        
            for key in arr:
                for i in range(len(li)):
                    if(li[i]==key):
                        count=count+arr[key]
                        print(count)
      
        
        return count
        

sol=Solution()
sol.romanToInt('IV')

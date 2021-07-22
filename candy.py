def kidsWithCandies(candies, extraCandies):
        n=0
        mx=max(candies)
        m=len(candies)-1
        print(mx)
        while m>=0:
            if candies[n] + extraCandies >=mx:
                print(candies)
                candies[n]=True
            else:
                candies[n]=False
            m-=1
            n+=1
        return candies

print(kidsWithCandies([2,3,5,1,3],3))
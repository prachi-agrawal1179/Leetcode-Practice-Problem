class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count=0
        if(N==1):
            return(1)
        else:
            for i in range(1,N):
                prev=i*(i-1)//2;
                temp=(N+prev)//i;
                if(temp==(N+prev)/i and temp-(i-1)!=0):
                    count=count+1
                if(temp-(i-1)==0):
                    break
            return(count)

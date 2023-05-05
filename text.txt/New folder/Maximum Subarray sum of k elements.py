
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        wstart=0
        wend=0
        ans=0
        s=0
        while(wend<N):
            s+=Arr[wend]
            if((wend-wstart+1)==K):
                ans=max(ans,s)
                s-=Arr[wstart]
                wstart=wstart+1
                
            wend=wend+1
        return ans

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        char={}
        res=0
        while j<len(s):
           # res=max(res,j-i+1)
            char[s[j]]=char.get(s[j],0)+1
            while max(char.values())+k<j-i+1 and i<=j:
                char[s[i]]-=1
                i+=1
                
            j+=1
            res=max(res,j-i)
            
        return res
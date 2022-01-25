class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt = 1
        ans = s[0]
        for i in range(1,len(s)):
            if s[i] == s[i-1] :
                cnt +=1
            else :
                cnt = 1
            if cnt < 3:
                ans += s[i]
        return ans
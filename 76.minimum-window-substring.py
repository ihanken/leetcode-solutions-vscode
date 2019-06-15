#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import Counter

class Solution:
    def contains(self, container, contained):
        return all(container[x] >= contained[x] for x in contained)

    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        
        if n > m: return ""
        
        minString = ""
        sCounter = Counter()
        tCounter = Counter(t)
        
        i = 0
        j = 0
        
        while i <= j < len(s):
            sCounter[s[j]] += 1
            
            while self.contains(sCounter, tCounter) and i <= j:
                if minString == "" or len(minString) > (j - i) + 1:
                    minString = s[i:j + 1]
                
                sCounter[s[i]] -= 1
                
                if sCounter[s[i]] <= 0: del sCounter[s[i]]
                
                i += 1
            else:
                j += 1
                
        return minString
        
        


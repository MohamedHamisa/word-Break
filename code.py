class Solution():
    def wordBreak(self, s, wordDict):
        memo, words = {len(s): ['']}, set(wordDict)
        ss = set(len(x) for x in words)
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in [i + x for x in ss]
                           if s[i:j] in words
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)

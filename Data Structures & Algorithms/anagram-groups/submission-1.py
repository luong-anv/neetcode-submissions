class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash =  {}
        res = []
        for word in strs:
            word_sorted =''.join(sorted(word))
            if word_sorted not in hash.keys():
                hash[word_sorted] = [word]
            else:
                hash[word_sorted].append(word)
        return  [res for res in hash.values()]



        
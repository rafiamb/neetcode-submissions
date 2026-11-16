class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for str in strs:
            freq = [0] * 26
            for ch in str:
                freq[ord(ch) - ord('a')] += 1

            tup = tuple(freq)
            
            if tup not in output:
                output[tup] = [str]
            else:
                output[tup].append(str)

        return(list(output.values()))

            

    

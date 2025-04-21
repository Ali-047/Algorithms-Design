import tkinter as tk
import hashlib
import difflib
# Bloom Filter implementation
class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hash(self, item, seed):
        hash_obj = hashlib.md5((item + str(seed)).encode('utf-8'))
        hash_digest = hash_obj.hexdigest()
        return int(hash_digest, 16) % self.size
    
    def add (self, item ):
        for seed in range (self.hash_count):
            self.bit_array[self._hash(item , seed)] = 1
            
            
    def check(self, item):
        for seed in range(self.hash_count):
            if self.bit_array[self._hash(item, seed)] == 0:
                return False
        return True

# Jaccard Similarity function (using word tokens)
def jaccard_similarity(set1, set2):
    intersection = len(set(set1).intersection(set2))
    union = len(set(set1).union(set2))
    return intersection / union if union != 0 else 0


                    # Levenshtein Distance function
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Compute the Levenshtein distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]
 
            
    # Function to extract common identical sequences (including spaces) using difflib.
def get_common_sequences(s1, s2, min_len=2):
    """
    Returns a list of common identical substrings between s1 and s2
    that have a length of at least min_len.
    """
    matcher = difflib.SequenceMatcher(None, s1, s2)
    blocks = matcher.get_matching_blocks()[:-1]  # Remove the dummy block.
    common = []
    for block in blocks:
        if block.size >= min_len:
            substring = s1[block.a: block.a + block.size]
            if substring not in common:
                common.append(substring)
    return common
        
        
         
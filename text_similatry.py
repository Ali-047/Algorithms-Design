import hashlib
import difflib

class BloomFilter:
    def __init__(self, size, hash_count):
        try:
            if not isinstance(size, int) or not isinstance(hash_count, int):
                raise TypeError("Size and hash_count must be integers")
            if size <= 0 or hash_count <= 0:
                raise ValueError("Size and hash_count must be positive")
            self.size = size
            self.hash_count = hash_count
            self.bit_array = [0] * size
        except (TypeError, ValueError) as e:
            raise e

    def _hash(self, item, seed):
        try:
            hash_obj = hashlib.md5((str(item) + str(seed)).encode('utf-8'))
            hash_digest = hash_obj.hexdigest()
            return int(hash_digest, 16) % self.size
        except Exception as e:
            raise ValueError(f"Error in hashing: {str(e)}")
    
    def add(self, item):
        try:
            for seed in range(self.hash_count):
                self.bit_array[self._hash(item, seed)] = 1
        except Exception as e:
            raise ValueError(f"Error adding item to Bloom filter: {str(e)}")
            
    def check(self, item):
        try:
            for seed in range(self.hash_count):
                if self.bit_array[self._hash(item, seed)] == 0:
                    return False
            return True
        except Exception as e:
            raise ValueError(f"Error checking item in Bloom filter: {str(e)}")

def jaccard_similarity(set1, set2):
    try:
        if not isinstance(set1, (set, list, tuple)) or not isinstance(set2, (set, list, tuple)):
            raise TypeError("Inputs must be sets, lists, or tuples")
        set1, set2 = set(set1), set(set2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        if union == 0:
            return 0
        return intersection / union
    except TypeError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error calculating Jaccard similarity: {str(e)}")

def levenshtein_distance(s1, s2):
    try:
        if not isinstance(s1, str) or not isinstance(s2, str):
            raise TypeError("Inputs must be strings")
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[m][n]
    except TypeError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error calculating Levenshtein distance: {str(e)}")

def get_common_sequences(s1, s2, min_len=2):
    try:
        if not isinstance(s1, str) or not isinstance(s2, str):
            raise TypeError("Inputs must be strings")
        if not isinstance(min_len, int) or min_len < 1:
            raise ValueError("min_len must be a positive integer")
            
        matcher = difflib.SequenceMatcher(None, s1, s2)
        blocks = matcher.get_matching_blocks()[:-1]
        common = []
        for block in blocks:
            if block.size >= min_len:
                substring = s1[block.a: block.a + block.size]
                if substring not in common:
                    common.append(substring)
        return common
    except (TypeError, ValueError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error finding common sequences: {str(e)}")

def analyze_similarity(text1, text2):
    try:
        if not isinstance(text1, str) or not isinstance(text2, str):
            raise TypeError("Both inputs must be strings")
        if not text1 or not text2:
            raise ValueError("Both texts must not be empty")

        text1, text2 = text1.strip(), text2.strip()
        
        # Initialize Bloom filter and process words
        bloom_filter = BloomFilter(size=1000, hash_count=3)
        words1 = text1.lower().split()
        words2 = text2.lower().split()
        
        # Add words to Bloom filter and check overlap
        for word in words1:
            bloom_filter.add(word)
        
        bloom_matches = sum(1 for word in words2 if bloom_filter.check(word))
        bloom_similarity = bloom_matches / len(words2) if words2 else 0
        
        # Calculate Jaccard similarity
        jaccard_score = jaccard_similarity(words1, words2)
        
        # Calculate normalized Levenshtein distance
        lev_distance = levenshtein_distance(text1.lower(), text2.lower())
        max_len = max(len(text1), len(text2))
        lev_similarity = 1 - (lev_distance / max_len if max_len > 0 else 0)
        
        # Calculate overall similarity score (weighted average)
        similarity_score = round((bloom_similarity * 0.3 + jaccard_score * 0.4 + lev_similarity * 0.3) * 100)
        
        return similarity_score
        
    except (TypeError, ValueError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error analyzing text similarity: {str(e)}")
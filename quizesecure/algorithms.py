# bloom filter alghorithm

from hashlib import md5
import hashlib
from random import seed


class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

        def _hash(Self, item):
            hash_obj = hashlib.md5((item + str(seed)).encode('utf-8'))
            hash_digest = hash_obj.hexdigest()
            return int(hash_digest, 16) % self.size

        def add(self, item):
            for seed in range(self.hash_count):
                result = self._hash(item, seed)
                self.bit_array[result] = 1

                def cheack(self, item):
                    for seed in range(self.hash_count):
                        result = self._hash(item, seed)
                        if self.bit_arrat[result] == 0:
                            return False
                        return True


def jacard_similatary(set1, set2):
    intersection = len(set(set1).intersection(set2))
    union = len(set(set1).union(set2))
    return intersection / union


def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # input
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # محاسبه فاصله لِوِنِشتاین
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]

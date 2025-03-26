#bloom filter alghorithm 
from hashlib import md5
import hashlib
from random import seed


class BloomFilter:
    def __init__(self,size ,hash_count):
        self.size = size 
        self.hash_count = hash_count
        self.bit_array = [0] * size 
        
        def _hashe (Self , item):
            hash_obj = hashlib.md5((item + str(seed)).encode('utf-8'))
                  
        
        

        
        
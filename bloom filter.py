#bloom filter alghorithm 

from hashlib import md5
import hashlib
from random import seed


class BloomFilter:
    def __init__(self,size ,hash_count):
        self.size = size 
        self.hash_count = hash_count
        self.bit_array = [0] * size 
        
        def _hash (Self , item):
            hash_obj = hashlib.md5((item + str(seed)).encode('utf-8'))
            hash_digest = hash_obj.hexdigest()
            return int(hash_digest , 16 ) % self.size
        
        def add(self , item ) :
            for seed in range (self.hash_count):
                result = self ._hash(item , seed)
                self.bit_array[result]=1
                
                def cheack (self , item):
                 for seed in range (self.hash_count):
                     result = self._hash(item , seed ) 
                     if self.bit_arrat[result] == 0:
                         return False
                     return True
                 
                 
              


        

        
        
import tkinter as tk
import hashlib
import difflib

# Bloom filter implementation

class BloomFilter:
    def __init__(self , size , hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
        
        def _hash (self , item , seed)
        hash_obj = hashlib.md5((item + str(seed)).encode('utf-8'))
        
        
         
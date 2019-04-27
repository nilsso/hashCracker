#!/usr/bin/env python3
import unittest
from os import path
from sys import exit
from hashlib import md5, sha1, sha256
from hashCracker import hashCracker as HC

wordfile_path = './rockyou.txt'

if not path.isfile(wordfile_path):
    print(f'''\
Could not find "{wordfile_path}" word file
Available at: <https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt>''')
    exit()


md5_hashes = [
        'dbe7e69e0992132f4a18394556ef8720',
        'e6c155570d6ff6464619a887076b6e36']
md5_cracks = [
        'wellard1',
        'aron2006']

class HashCrackerTests(unittest.TestCase):
    def test_md5_all(self):
        _solved = list(zip(md5_hashes, md5_cracks))
        _unsolved = []
        solved, unsolved = HC(md5, wordfile_path, md5_hashes)
        self.assertEqual(solved, _solved)
        self.assertEqual(unsolved, _unsolved)

if __name__ == '__main__':
    unittest.main()
        

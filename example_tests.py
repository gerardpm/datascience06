# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:22:46 2015

@author: gerar_000
"""

import sys
import math
import os.path
import re
import textwrap
import optparse
import xml.parsers.expat
import collections
import locale
import json

def fizzbuzz_test(f):
    if f(3) == "fizz" and f(5) == "buzz" and f(15) == "fizzbuzz":
        print("Success!")
    else:
        print("Nope. Try again.")

def fizzbuzz(n):
    ret = ""
    if not (n%3):
        ret += "fizz"
    if not (n%5):
        ret += "buzz"
    return ret or str(n)

import unittest
import cProfile 

cProfile.runctx('fizzbuzz_test', globals(), locals(), 'output_file')

class ExampleTests(unittest.TestCase):
        fizzbuzz_test(fizzbuzz)
if __name__ == "__main__":
    unittest.main()
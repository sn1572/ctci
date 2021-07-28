# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 08:23:03 2021

@author: sn1572
"""


import unittest
from chapter_1 import (sol_1, sol_4, sol_5)


class Test_Sol_1(unittest.TestCase):
    def test_1(self):
        val = sol_1('asdf')
        self.assertEqual(val, True)

    def test_2(self):
        self.assertEqual(sol_1('asdfa'), False)

    def test_3(self):
        self.assertEqual(sol_1(''), True)

    def test_4(self):
        words = '''
                this is a hella long string with a bunch
                of @#$^%7 random &*_Z characters in it. But
                it's definitely not all unique characters.
                Hell, the word character has two a's!
                '''
        self.assertEqual(sol_1(words), False)

    def test_5(self):
        basic_fail = 'aa'
        self.assertEqual(sol_1(basic_fail), False)


class Test_Sol_4(unittest.TestCase):
    def test_1(self):
        ex = 'tact Coa'
        self.assertEqual(sol_4(ex), True)

    def test_2(self):
        ex = 'not a permutation of a palindrome'
        self.assertEqual(sol_4(ex), False)

    def test_3(self):
        ex = ''
        self.assertEqual(sol_4(ex), True)


class Test_Sol_5(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sol_5('pale', 'ple'), True)

    def test_2(self):
        self.assertEqual(sol_5('pales', 'pale'), True)

    def test_3(self):
        self.assertEqual(sol_5('pale', 'bale'), True)

    def test_4(self):
        self.assertEqual(sol_5('pale', 'bake'), False)

    def test_5(self):
        self.assertEqual(sol_5('', 'a'), True)

    def test_6(self):
        self.assertEqual(sol_5('ahawe4ot7awoegf',
                               'ahawe4otawoegf'), True)



if __name__ == '__main__':
    unittest.main()
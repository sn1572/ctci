# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 08:19:38 2021

@author: sn1572
"""


from collections import defaultdict


def sol_1(string):
    char_dict = defaultdict(int)
    for char in string:
        if char_dict[char] > 0:
            return(False)
        char_dict[char] += 1
    return(True)


def sol_3(string):
    '''
    This one is so easy in Python there's almost no point.
    '''
    return(string.replace(' ', '%20'))


def sol_4(string):
    string = string.replace(' ', '').lower()
    char_dict = defaultdict(int)
    for char in string:
        char_dict[char] += 1
    num_ones = 0
    for val in char_dict.values():
        if val > 2:
            return(False)
        if val == 1:
            num_ones += 1
            if num_ones > 1:
                return(False)
        elif val < 1:
            return(False)
    return(True)


def sol_5(string1, string2):

    def swap(string1, string2):
        '''
        Checks if string2 is the same as string1, with
        at most one character switched. Will return True
        if the strings are equal.
        '''
        if len(string1) != len(string2):
            return(False)
        swapped = 0
        for i, char in enumerate(string1):
            if string2[i] != char:
                swapped += 1
            if swapped > 1:
                return(False)
        return(True)

    def add(string1, string2):
        '''
        Checks if string2 is equal to string1 with
        an added character.
        '''
        if len(string1)+1 != len(string2):
            return(False)
        skip = 0
        for i, char in enumerate(string1):
            if char != string2[i+skip]:
                skip += 1
            if skip > 1:
                return(False)
        return(True)

    def delete(string1, string2):
        '''
        Checks if string2 is equal to string1 with
        one deleted character.
        '''
        if len(string1) < len(string2):
            string1, string2 = string2, string1
        return(add(string2, string1))

    return(swap(string1, string2) or add(string1, string2) or delete(string1,
                                                                     string2))
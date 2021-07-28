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

    def compare(dict1, dict2):
        diffs = 0
        for key, val in dict1.items():
            if key not in dict2:
                diffs += 1
            elif dict2[key] != val:
                diffs += 1
        return(diffs)

    def get_char_dict(string):
        char_dict = defaultdict(int)
        for char in string:
            char_dict[char] += 1
        return(char_dict)

    char_dict_1 = get_char_dict(string1)
    char_dict_2 = get_char_dict(string2)
    diffs = compare(char_dict_1, char_dict_2)
    if diffs > 1:
        return False
    diffs += compare(char_dict_2, char_dict_1)
    if diffs > 1:
        return(False)
    return(True)
    
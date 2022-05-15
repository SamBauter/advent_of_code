"""Inventory Management"""
from typing import Counter


with open("2018/2-input.txt", "r") as f:
    s = f.read()

def inv_man(s: str) -> int:
    twos = 0
    threes = 0
    for line in s.splitlines():
        found3 = False
        found2 = False
        for c in line:
            count = line.count(c)
            if found2 and found3:
                break
            elif count==3 and not found3:
                threes+=1
                found3= True
            elif count==2 and not found2:
                twos+=1
                found2= True
    return twos*threes


def single_diff(s1: str, s2: str) -> bool:
    total_diff = 0
    for c1,c2 in zip(s1,s2):
        if c1 != c2:
            total_diff+=1
        if total_diff > 1:
            return False
    if total_diff ==1:
        return True
    return False

def get_same_chars(s1: str, s2: str) -> str:
    same_char = ''
    for c1,c2 in zip(s1,s2):
        if c1==c2:
            same_char+=c1
    return same_char


def one_char_diff(s: str) -> str:
    line_list = s.splitlines()
    compare_list = line_list.copy()
    for line in line_list:
        compare_list.remove(line)
        for comp_line in compare_list:
            if single_diff(comp_line,line):
                return get_same_chars(comp_line,line)
        


#print(inv_man("abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab\n"))
#print(inv_man(s))
#print(one_char_diff(s))

"""Solutions inspired by anthony_codes pseudocode"""
def check_sum1(s:str) -> int:
    threes = 0
    twos = 0
    for line in s.splitlines():
        c= Counter(line)
        if 3 in c.values():
            threes+=1
        if 2 in c.values():
            twos+=1
    return twos*threes



print(check_sum1(s))

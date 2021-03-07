"""
주어진 문자가 팰린드롬 문자인지 확인하는 문제
"""
import collections

# input_str = str(input())
# input_str = input_str.upper()
# input_str = input_str.replace(" ", "")
#
# output_str_reverse = ""
# output_str = ""
# for ch in input_str:
#     if (ord(ch) <= 90 and ord(ch) >= 65) or (ord(ch)<=57 and ord(ch) >= 48):
#         output_str_reverse += ch
#         output_str += ch
#
# print(list(output_str_reverse).reverse() == list(output_str))

# 책 풀이
# 01. 리스트로 변환
import re

def isPalindromebyList(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    #팰린드롬 여부를 판단
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

def isPalindromebyDeque(s: str)-> bool:
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

def isPalindromebySlicing(s :str) -> bool:
    s = s.lower()

    s = re.sub('\W','',s)

    return s == s[::-1]


# input_str = str(input())

input_str = "a man a plan a canal : Panama"
# print(isPalindromebySlicing(input_str))



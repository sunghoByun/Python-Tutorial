
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys
input = sys.stdin.readline
from collections import deque
import copy
import itertools

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def main(begin, target, words):

    def dif(begin, target):
        difference = 0
        for i in range(len(begin)):
            if begin[i] != target[i]:
                difference +=1
        return difference

    graph = [[0 for _ in range(len(words ) +1)] for _ in range(len(words ) +1)]

    words.insert(0 ,begin)

    for i in range(len(words)):
        for j in range(len(words)):
            if i== j:
                continue
            elif dif(words[i], words[j]) == 1:
                graph[i][j] = 1

                begin_idx = words.index(begin)

    print(begin_idx)
    # def dfs(begin_idx, target_idx, graph):

    if target not in words:
        print(0)
    else:
        print(graph)

    answer = 0
    return answer


main(begin, target, words)

answer = 0

def dfs(begin, target, words, visited):
    global answer
    stacks = [begin]

    while stacks:
        # 스택을 활용한 dfs 구현
        stack = stacks.pop()
        if stack == target:
            return answer

        for w in range(0, len(words)):
            # 조건 1. 한 개의 알파벳만 다른 경우
            if len([i for i in range(0, len(words[w])) if words[w][i] != stack[i]]) == 1:
                if visited[w] != 0: continue
                visited[w] = 1
                # stack에 추가
                stacks.append(words[w])
        # depth +
        answer += 1


def solution(begin, target, words):
    global answer

    # 조건 2. words에 있는 단어로만 변환할 수 있습니다.
    if target not in words:
        return 0

    visited = [0 for i in words]
    dfs(begin, target, words, visited)

    return answer

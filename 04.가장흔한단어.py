"""금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력"""
import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

def mostCommonWord(paragraph : str, banned : list) -> str:
    paragraph = re.sub('[\W]',' ', paragraph)

    words = [word for word in paragraph.lower().split() if word not in banned]

    a = collections.Counter(words)

    return a.most_common(1)[0][0]


print(mostCommonWord(paragraph= paragraph, banned=banned))
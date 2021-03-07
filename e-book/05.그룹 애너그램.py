"""
list 와 string

list가 가진 다양한 기능

list.index(value) : 값을 이용하여 위치를 찾음

    list1 = ['a','b','q','f']
    list1.index('q')
    >> 2

list.extend([value1, value2]) : 리스트 뒤에 값을 추가 '+' 연산자보다 성능 좋음

    list2 = [1,2,3]
    list1.extend(list2)

    list1
    >>['a','b','q','f',1,2,3]

list.insert(index, value) : 원하는 위치에 값ㅇ르 추가

list <--> str

str -> list
    list = str.split()
list -> str
    ''.join(list)

    time_str = "10:34:17"
    time_list = time_str.split(':')
    time_list
    >> ['10','34','17']

    ':'.join(time_list)
    >> '10:34:17'

"""



"""
print(sorted("This is a test string from Andrew".split()))


class Student:
    def __init__(self, name, grade, age):
        self.selfName = name
        self.selfGrade = grade
        self.selfAge = age

    def __repr__(self):
        return repr((self.selfName, self.selfGrade, self.selfAge))

student_Object = [
    Student('John','A','15'),
    Student('JANE','B','12'),
    Student('DAVE','B','10')
]

print(sorted(student_Object, key = lambda student: student.selfAge))

print(student_Object)

c = ['aaab', 'aaaa','aac','ad']
print(sorted(c,key=len))

def fn(s):
    return s[0],s[-1]

print(sorted(c,key=fn))

"""

import collections

words = ["eat","tea","tan", "ate", "nat", "bat"]

def groupAnagrams(self,strs : list):

    anagram=collections.defaultdict(list)

    for word in strs:
        anagram[''.join(sorted(word))].append(word)

    return list(anagram.values())

print(groupAnagrams("",strs=words))


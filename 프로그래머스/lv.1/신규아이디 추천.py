
ids = "=.="

def solution(new_id1):
    #1단계
    new_id1 = new_id1.lower()

    #2단계
    new_id2 = ''
    for ch in new_id1:
        if ch.isalnum() or ch in '-_.':
            new_id2+= ch

    #3단계
    while '..' in new_id2:
        new_id2 = new_id2.replace('..','.')

    #4단계
    if new_id2[0] == '.':
        new_id2 = new_id2[1:]
    elif new_id2[-1] == '.':
        new_id2 = new_id2[:-1]

    #5단계
    while len(new_id2)< 1:
        new_id2 += "a"

    #6단계
    if len(new_id2) >= 16 :
        new_id2 = new_id2[:15]

    if  new_id2[-1] == '.':
        new_id2 = new_id2[:-1]

    #7단계
    if len(new_id2) <=2 :
        while len(new_id2) < 3 :
            new_id2 += new_id2[-1]

    return new_id2

print(solution(ids))
import collections
import math
from datetime import datetime

# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

def solution(fees,records):
    basicTime = fees[0]
    basicFee = fees[1]
    minutes = fees[2]
    fee = fees[3]

    carRecordIn = collections.OrderedDict()
    carRecordOut = collections.OrderedDict()
    carRecordInOut = dict()

    for record in records:
        recordList = record.split()
        if recordList[2] == "IN":
            if recordList[1] not in carRecordIn.keys():
                carRecordInOut[recordList[1]] = 0
                carRecordIn[recordList[1]] = [recordList[0]]
            else : carRecordIn[recordList[1]].append(recordList[0])
        else :
            if recordList[1] not in carRecordOut.keys():
                carRecordOut[recordList[1]] = [recordList[0]]
            else:
                carRecordOut[recordList[1]].append(recordList[0])

    for key in carRecordIn.keys():
        # print(key)
        if key not in carRecordOut.keys():
            carRecordOut[key] = ['23:59']

        tmpCarIn = carRecordIn[key]
        tmpCarOut = carRecordOut[key]
        if len(tmpCarIn) > len(tmpCarOut) : tmpCarOut.append('23:59')

        for i in range(len(carRecordIn[key])):

            time_1 = datetime.strptime(tmpCarIn[i], "%H:%M")
            time_2 = datetime.strptime(tmpCarOut[i], "%H:%M")
            diff = time_2 - time_1

            diffMinutes = diff.seconds/60
            carRecordInOut[key] += diffMinutes

    carRecordInOut = sorted(carRecordInOut.items())

    answer = []

    for tmp in carRecordInOut:
        if tmp[1] <= basicTime:
            ans = basicFee
        else:
            ans = basicFee + int(math.ceil((tmp[1] - basicTime)/minutes)) * fee

        answer.append(ans)

    return answer

print(solution(fees,records))



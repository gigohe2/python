# 50명의 승객과 매칭 기회, 총 탑승 승객수를 구하라
# 조건 1: 운행 소요 시간 5~50분 사이의 난수로 정해짐
# 조건 2: 소요 시간 5~15분 사이의 승객만 매칭

# [O] 1번째 손님 ( 소요시간 : 15분)
# [ ] 2번재 손님 (소요시간 : 50분)
# 총 탑승 승객 : N 분

from random import *
cnt = 0
for i in range(1,51): # 50명
    time = randrange(5,51)
    if 5<=time<=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))

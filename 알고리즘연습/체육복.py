lost = [2, 4]
reserve = [3, 1]
n=5

answer = n
same = list(set(lost) & set(reserve)) # 교집합
for i in same: # 중복되는 것 제거 완료
    lost.remove(i)
    reserve.remove(i)

print("lost:{0}, reserve:{1}".format(lost,reserve))
num = len(lost)
num2 = len(reserve)
k = 0
flag = 0
for i in range(0, num):
    print("{0}가 빌릴수있는지 검사".format(lost[i]))
    flag = 0
    for j in range(0, num2):
        print("{0}가 {1}에게 빌려줄 수 있을까?".format(reserve[j], lost[i]))
        if abs(int(lost[i])-int(reserve[j])) <=1: # 빌려줄 수 있으면
            print("{0}가 {1}에게 빌려줄 수 있다. 차이는 {2}".format(reserve[j], lost[i],abs(int(lost[i])-int(reserve[j]))))
            reserve.remove(int(reserve[j])) # 빌린 체육복은 제외시킨다
            num2 -= 1
            flag = 1
            break
    if flag == 0:
        answer -= 1

print(answer)
        
        
    

print(answer)
gun = 10 # 전역변수

def checkpoint(soldiers):
    global gun # 전역변수 gun을 함수 내에서 사용한다.
    gun = gun - soldiers #지역변수
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers # 지역 변수 gun 사용함
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2)

print("전체 총 : {0}".format(gun))

gun = checkpoint_ret(gun, 3)
print("전체 총 : {0}".format(gun))